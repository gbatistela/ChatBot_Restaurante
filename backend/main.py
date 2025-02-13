# Author: Dhaval Patel. Codebasics YouTube Channel 

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import logging
import db_helper
import generic_helper
from db_helper import get_all_orders
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Permitir solicitudes desde cualquier origen (en producción puedes restringirlo a dominios específicos)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://mi-frontend.vercel.app"],  # Agrega el dominio de tu frontend en producción
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Logger para depuración
logging.basicConfig(level=logging.INFO)

# Diccionario para órdenes en progreso
inprogress_orders = {}



# Ruta raíz para solicitudes GET
@app.get("/")
async def root():
    return {"message": "Restaurant Chatbot API is running!"}


@app.get("/orders")
def get_orders():
    orders = get_all_orders()  # Obtiene las órdenes de la base de datos
    return {"orders": orders}


# Ruta para manejar solicitudes POST desde Dialogflow
@app.post("/")
async def handle_request(request: Request):
    # Registrar la solicitud entrante
    payload = await request.json()
    logging.info(f"Received payload: {payload}")

    # Extraer información clave del payload
    try:
        intent = payload['queryResult']['intent']['displayName']
        parameters = payload['queryResult']['parameters']
        output_contexts = payload['queryResult']['outputContexts']
        session_id = generic_helper.extract_session_id(output_contexts[0]["name"])

        # Diccionario de handlers para los intents
        intent_handler_dict = {
            'order.add - context: ongoing-order': add_to_order,
            'order.remove - context: ongoing-order': remove_from_order,
            'order.complete - context: ongoing-order': complete_order,
            'track.order - context: ongoing-tracking': track_order
        }

        # Verificar si el intent está definido
        if intent not in intent_handler_dict:
            return JSONResponse(content={
                "fulfillmentText": f"Sorry, I couldn't handle the intent '{intent}'."
            })

        # Ejecutar el handler correspondiente
        return intent_handler_dict[intent](parameters, session_id)

    except KeyError as e:
        logging.error(f"Missing key in payload: {e}")
        return JSONResponse(content={
            "fulfillmentText": "An error occurred while processing your request. Please try again."
        })

# Función para guardar la orden en la base de datos
def save_to_db(order: dict):
    next_order_id = db_helper.get_next_order_id()

    # Insertar elementos individuales en la tabla de órdenes
    for food_item, quantity in order.items():
        rcode = db_helper.insert_order_item(
            food_item,
            quantity,
            next_order_id
        )

        if rcode == -1:
            return -1

    # Insertar el estado de seguimiento del pedido
    db_helper.insert_order_tracking(next_order_id, "in progress")

    return next_order_id

# Handler para completar una orden
def complete_order(parameters: dict, session_id: str):
    if session_id not in inprogress_orders:
        fulfillment_text = "I'm having a trouble finding your order. Sorry! Can you place a new order please?"
    else:
        order = inprogress_orders[session_id]
        order_id = save_to_db(order)
        if order_id == -1:
            fulfillment_text = "Sorry, I couldn't process your order due to a backend error. Please place a new order again."
        else:
            order_total = db_helper.get_total_order_price(order_id)
            fulfillment_text = f"¡Genial! Hemos realizado su pedido. " \
                               f"Aquí está el número de pedido n.° {order_id}. " \
                               f"El total de su pedido es de {order_total} que puede pagar al momento de la entrega.!"
            

        del inprogress_orders[session_id]

    return JSONResponse(content={
        "fulfillmentText": fulfillment_text
    })

# Handler para agregar elementos a una orden
def add_to_order(parameters: dict, session_id: str):
    food_items = parameters.get("food-item", [])
    quantities = parameters.get("number", [])

    if len(food_items) != len(quantities):
        fulfillment_text = "Sorry, I didn't understand. Can you please specify food items and quantities clearly?"
    else:
        new_food_dict = dict(zip(food_items, quantities))

        if session_id in inprogress_orders:
            current_food_dict = inprogress_orders[session_id]
            current_food_dict.update(new_food_dict)
            inprogress_orders[session_id] = current_food_dict
        else:
            inprogress_orders[session_id] = new_food_dict

        order_str = generic_helper.get_str_from_food_dict(inprogress_orders[session_id])
        fulfillment_text = f"Hasta ahora tienes: {order_str}. ¿Necesitas algo más?"

    return JSONResponse(content={
        "fulfillmentText": fulfillment_text
    })

# Handler para eliminar elementos de una orden
def remove_from_order(parameters: dict, session_id: str):
    if session_id not in inprogress_orders:
        return JSONResponse(content={
            "fulfillmentText": "I'm having trouble finding your order. Sorry! Can you place a new order please?"
        })
    
    food_items = parameters.get("food-item", [])
    current_order = inprogress_orders[session_id]

    removed_items = []
    no_such_items = []

    for item in food_items:
        if item not in current_order:
            no_such_items.append(item)
        else:
            removed_items.append(item)
            del current_order[item]

    fulfillment_text = ""
    if removed_items:
        fulfillment_text += f"Removed {', '.join(removed_items)} from your order!"
    if no_such_items:
        fulfillment_text += f" Your current order does not have {', '.join(no_such_items)}."
    if not current_order:
        fulfillment_text += " Your order is empty!"
    else:
        order_str = generic_helper.get_str_from_food_dict(current_order)
        fulfillment_text += f" Here is what is left in your order: {order_str}"

    return JSONResponse(content={
        "fulfillmentText": fulfillment_text
    })


# Handler para rastrear una orden
def track_order(parameters: dict, session_id: str):
    try:
        # Obtener el 'order_id' desde los parámetros
        order_id = parameters.get('number')
        
        # Validar si el número es válido
        if order_id is None:
            return JSONResponse(content={
                "fulfillmentText": "Por favor, proporciona un ID de pedido válido para rastrear la orden."
            })

        # Convertir el parámetro a entero si es necesario
        try:
            order_id = int(order_id)
        except ValueError:
            return JSONResponse(content={
                "fulfillmentText": "El ID de pedido proporcionado no es válido. Por favor, ingresa un número válido."
            })

        # Llamar a la base de datos para obtener el estado del pedido
        order_status = db_helper.get_order_status(order_id)

        # Verificar si se encontró el pedido
        if order_status:
            fulfillment_text = f"El estado actual del pedido con ID {order_id} es: {order_status}."
        else:
            fulfillment_text = f"No se encontró ningún pedido con el ID: {order_id}."

    except Exception as e:
        # Manejar cualquier excepción general
        fulfillment_text = f"Ocurrió un error al rastrear la orden: {str(e)}"

    # Retornar la respuesta como JSON
    return JSONResponse(content={
        "fulfillmentText": fulfillment_text
    })

""" 

git add .
git commit -m "3"
git push origin main
"""
