import sqlite3

# Ruta a tu archivo de base de datos SQLite
db_path = 'C:\\Users\\Flia Caro Sosa Veron\\OneDrive\\Desktop\\Proyecto-AESTETHIC\\instance\\Aestethic.db'

# Conectar a la base de datos
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Pedir al usuario que ingrese los IDs de usuarios que desea eliminar
ids_a_eliminar = input("Ingrese los IDs de los usuarios que desea eliminar, separados por comas: ")

# Convertir los IDs en una lista de enteros
ids_a_eliminar = [int(id.strip()) for id in ids_a_eliminar.split(",")]

# Eliminar usuarios específicos
try:
    # Crear una cadena de IDs separados por coma para usar en la consulta SQL
    placeholders = ', '.join('?' for _ in ids_a_eliminar)
    query = f"DELETE FROM users WHERE id IN ({placeholders});"
    cursor.execute(query, ids_a_eliminar)
    conn.commit()
    print(f"Los usuarios con ID {ids_a_eliminar} han sido eliminados.")
except sqlite3.OperationalError as e:
    print(f"Error al eliminar usuarios: {e}")

# Cerrar la conexión
conn.close()

