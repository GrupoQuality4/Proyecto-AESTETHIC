import sqlite3

db_path = 'C:\\Users\\Tecno\\Desktop\\Proyecto-AESTETHIC\\instance\\Aestethic.db'
#db_path = 'C:\\Users\\Flia Caro Sosa Veron\\OneDrive\\Desktop\\Proyecto-AESTETHIC\\instance\\Aestethic.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

ids_a_eliminar = input("Ingrese los IDs de los usuarios que desea eliminar, separados por comas: ")
ids_a_eliminar = [int(id.strip()) for id in ids_a_eliminar.split(",")]

try:
    placeholders = ', '.join('?' for _ in ids_a_eliminar)
    query = f"DELETE FROM users WHERE user_id IN ({placeholders});"
    cursor.execute(query, ids_a_eliminar)
    conn.commit()
    print(f"Los usuarios con ID {ids_a_eliminar} han sido eliminados.")
except sqlite3.OperationalError as e:
    print(f"Error al eliminar usuarios: {e}")

conn.close()



