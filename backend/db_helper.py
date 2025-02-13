import mysql.connector
import os
import logging
from dotenv import load_dotenv

# Configuración de logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

REQUIRED_ENV_VARS = ["DB_HOST", "DB_USER", "DB_PASSWORD", "DB_NAME"]

for var in REQUIRED_ENV_VARS:
    if not os.getenv(var):
        raise EnvironmentError(f"Missing required environment variable: {var}")

# Función para obtener una conexión a la base de datos
def get_connection():
    try:
        return mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
        )
    except mysql.connector.Error as e:
        logging.error(f"Error al conectar con la base de datos: {e}")
        return None

# Función para obtener todas las órdenes del restaurante
def get_all_orders():
    try:
        cnx = get_connection()
        if cnx is None:
            return []

        cursor = cnx.cursor(dictionary=True)
        query = """
            SELECT 
                o.order_id AS id, 
                GROUP_CONCAT(f.name SEPARATOR ', ') AS items, 
                SUM(o.quantity * f.price) AS total, 
                ot.status AS order_status
            FROM orders o
            JOIN food_items f ON o.item_id = f.item_id
            JOIN order_tracking ot ON o.order_id = ot.order_id
            GROUP BY o.order_id, ot.status
        """
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except mysql.connector.Error as err:
        logging.error(f"Error fetching orders: {err}")
        return []
    finally:
        if cnx:
            cnx.close()

# Función para insertar un ítem de pedido
def insert_order_item(food_item, quantity, order_id):
    try:
        cnx = get_connection()
        if cnx is None:
            return -1

        cursor = cnx.cursor()
        cursor.callproc('insert_order_item', (food_item, quantity, order_id))
        cnx.commit()
        logging.info("Order item inserted successfully!")
        return 1
    except mysql.connector.Error as err:
        logging.error(f"Error inserting order item: {err}")
        return -1
    finally:
        if cnx:
            cnx.close()

# Función para insertar un registro en la tabla de seguimiento de pedidos
def insert_order_tracking(order_id, status):
    try:
        cnx = get_connection()
        if cnx is None:
            return

        cursor = cnx.cursor()
        query = "INSERT INTO order_tracking (order_id, status) VALUES (%s, %s)"
        cursor.execute(query, (order_id, status))
        cnx.commit()
        logging.info("Order tracking record inserted successfully!")
    except mysql.connector.Error as err:
        logging.error(f"Error inserting order tracking record: {err}")
    finally:
        if cnx:
            cnx.close()

# Función para obtener el precio total de un pedido
def get_total_order_price(order_id):
    try:
        cnx = get_connection()
        if cnx is None:
            return None

        cursor = cnx.cursor()
        query = "SELECT get_total_order_price(%s)"
        cursor.execute(query, (order_id,))
        result = cursor.fetchone()
        return result[0] if result else None
    except mysql.connector.Error as err:
        logging.error(f"Error fetching total order price: {err}")
        return None
    finally:
        if cnx:
            cnx.close()

# Función para obtener el próximo ID de pedido disponible
def get_next_order_id():
    try:
        cnx = get_connection()
        if cnx is None:
            return 1

        cursor = cnx.cursor()
        query = "SELECT MAX(order_id) FROM orders"
        cursor.execute(query)
        result = cursor.fetchone()
        return result[0] + 1 if result and result[0] is not None else 1
    except mysql.connector.Error as err:
        logging.error(f"Error fetching next order ID: {err}")
        return 1
    finally:
        if cnx:
            cnx.close()

# Función para obtener el estado de un pedido
def get_order_status(order_id):
    try:
        cnx = get_connection()
        if cnx is None:
            return None

        cursor = cnx.cursor()
        query = "SELECT status FROM order_tracking WHERE order_id = %s"
        cursor.execute(query, (order_id,))
        result = cursor.fetchone()
        return result[0] if result else None
    except mysql.connector.Error as err:
        logging.error(f"Error fetching order status: {err}")
        return None
    finally:
        if cnx:
            cnx.close()

# Bloque principal para pruebas
if __name__ == "__main__":
    try:
        logging.info("Testing db_helper.py...")
        print("Next Order ID:", get_next_order_id())
    except Exception as e:
        logging.error(f"An error occurred during testing: {e}")
