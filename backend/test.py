# db_helper.py

import mysql.connector

# Establecer conexión con la base de datos
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root1234",
    database="pandeyji_eatery"
)



def get_order_status(order_id):
    """Obtiene el estado de un pedido desde la base de datos."""
    try:
        # Validar que order_id sea un entero
        if not isinstance(order_id, int):
            raise ValueError("El order_id debe ser un número entero.")

        # Crear un cursor utilizando el gestor 'with'
        with cnx.cursor() as cursor:
            # Consulta parametrizada para prevenir inyecciones SQL
            query = "SELECT status FROM order_tracking WHERE order_id = %s"
            cursor.execute(query, (order_id,))

            # Obtener el resultado de la consulta
            result = cursor.fetchone()

        # Retornar el estado del pedido si existe, o None si no existe
        return result[0] if result else None

    except mysql.connector.Error as err:
        print(f"Error de base de datos: {err}")
        return None

    except ValueError as ve:
        print(f"Error en los datos: {ve}")
        return None


def save_order(customer_name, order_status):
    """Función para guardar un nuevo pedido en la base de datos."""
    cnx = get_connection()
    cursor = cnx.cursor()

    query = """
        INSERT INTO orders (customer_name, order_status)
        VALUES (%s, %s)
    """
    cursor.execute(query, (customer_name, order_status))
    cnx.commit()

    # Recuperar el ID del nuevo pedido
    order_id = cursor.lastrowid

    cursor.close()
    cnx.close()

    return order_id

# Ejemplo de uso
if __name__ == "__main__":
    order_id = 123  # Reemplaza con un ID válido
    status = get_order_status(order_id)
    if status:
        print(f"El estado del pedido {order_id} es: {status}")
    else:
        print(f"No se encontró el pedido con ID {order_id}.")

