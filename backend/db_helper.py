import mysql.connector
import os
import logging
from dotenv import load_dotenv


# Configuración de logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


load_dotenv()  # Carga las variables de entorno desde el archivo .env

REQUIRED_ENV_VARS = ["DB_HOST", "DB_USER", "DB_PASSWORD", "DB_NAME"]

for var in REQUIRED_ENV_VARS:
    if not os.getenv(var):
        raise EnvironmentError(f"Missing required environment variable: {var}")


# Función para obtener una conexión a la base de datos
def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "root1234"),
        database=os.getenv("DB_NAME", "pandeyji_eatery")
    )

# Función para insertar un ítem de pedido utilizando un procedimiento almacenado
def insert_order_item(food_item, quantity, order_id):
    try:
        with get_connection() as cnx:
            with cnx.cursor() as cursor:
                cursor.callproc('insert_order_item', (food_item, quantity, order_id))
                cnx.commit()
        logging.info("Order item inserted successfully!")
        return 1
    except mysql.connector.Error as err:
        logging.error(f"Error inserting order item: {err}")
        return -1
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return -1

# Función para insertar un registro en la tabla de seguimiento de pedidos
def insert_order_tracking(order_id, status):
    try:
        with get_connection() as cnx:
            with cnx.cursor() as cursor:
                query = "INSERT INTO order_tracking (order_id, status) VALUES (%s, %s)"
                cursor.execute(query, (order_id, status))
                cnx.commit()
        logging.info("Order tracking record inserted successfully!")
    except mysql.connector.Error as err:
        logging.error(f"Error inserting order tracking record: {err}")

# Función para obtener el precio total de un pedido
def get_total_order_price(order_id):
    try:
        with get_connection() as cnx:
            with cnx.cursor() as cursor:
                query = "SELECT get_total_order_price(%s)"
                cursor.execute(query, (order_id,))
                result = cursor.fetchone()
        return result[0] if result else None
    except mysql.connector.Error as err:
        logging.error(f"Error fetching total order price: {err}")
        return None

# Función para obtener el próximo ID de pedido disponible
def get_next_order_id():
    try:
        with get_connection() as cnx:
            with cnx.cursor() as cursor:
                query = "SELECT MAX(order_id) FROM orders"
                cursor.execute(query)
                result = cursor.fetchone()
        return result[0] + 1 if result and result[0] is not None else 1
    except mysql.connector.Error as err:
        logging.error(f"Error fetching next order ID: {err}")
        return None

# Función para obtener el estado de un pedido
def get_order_status(order_id):
    try:
        with get_connection() as cnx:
            with cnx.cursor() as cursor:
                query = "SELECT status FROM order_tracking WHERE order_id = %s"
                cursor.execute(query, (order_id,))
                result = cursor.fetchone()
        return result[0] if result else None
    except mysql.connector.Error as err:
        logging.error(f"Error fetching order status: {err}")
        return None

# Bloque principal para pruebas
if __name__ == "__main__":
    try:
        logging.info("Testing db_helper.py...")
        print("Next Order ID:", get_next_order_id())
        # print(get_total_order_price(56))
        # insert_order_item('Samosa', 3, 99)
        # insert_order_tracking(99, "in progress")
    except Exception as e:
        logging.error(f"An error occurred during testing: {e}")



