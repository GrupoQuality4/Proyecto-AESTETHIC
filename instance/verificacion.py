import sqlite3

# Ruta a tu archivo de base de datos SQLite
db_path = 'C:\\Users\\Flia Caro Sosa Veron\\OneDrive\\Desktop\\Proyecto-AESTETHIC\\instance\\Aestethic.db'

# IDs de los tokens que deseas marcar como verificados
ids_a_verificar = input("Ingrese los IDs de los tokens que desea marcar como verificados, separados por comas: ")
ids_a_verificar = [int(id.strip()) for id in ids_a_verificar.split(",")]

# Conectar a la base de datos
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Actualizar tokens específicos
try:
    # Crear una cadena de placeholders para usar en la consulta SQL
    placeholders = ', '.join('?' for _ in ids_a_verificar)
    query = f"UPDATE verification_token SET is_used = 1 WHERE id IN ({placeholders});"
    cursor.execute(query, ids_a_verificar)
    conn.commit()
    print(f"Los tokens con ID {ids_a_verificar} han sido marcados como verificados.")
except sqlite3.OperationalError as e:
    print(f"Error al actualizar tokens: {e}")

# Cerrar la conexión
conn.close()
