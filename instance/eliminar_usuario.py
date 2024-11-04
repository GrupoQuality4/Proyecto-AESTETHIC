import sqlite3

<<<<<<< HEAD
db_path = 'C:\\Users\\Flia Caro Sosa Veron\\OneDrive\\Desktop\\Proyecto-AESTETHIC\\instance\\Aestethic.db'

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

def renombrar_tabla(old_name, new_name):
    rename_query = f"ALTER TABLE {old_name} RENAME TO {new_name};"
    cursor.execute(rename_query)
    conn.commit()
    print(f"Tabla '{old_name}' renombrada a '{new_name}'.")

renombrar_tabla('user', 'users')
=======
# Ruta a tu archivo de base de datos SQLite
#db_path = 'C:\\Users\\Tecno\\Desktop\\Proyecto-AESTETHIC\\instance\\Aestethic.db'
# O usa esta ruta si corresponde:
db_path = 'C:\\Users\\Flia Caro Sosa Veron\\OneDrive\\Desktop\\Proyecto-AESTETHIC\\instance\\Aestethic.db'

# Conectar a la base de datos
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Eliminar todas las reservas
try:
    cursor.execute("DELETE FROM reservas;")
    conn.commit()
    print("Todas las reservas han sido eliminadas.")
except sqlite3.OperationalError as e:
    print(f"Error al eliminar reservas: {e}")

# Cerrar la conexión
>>>>>>> 1a11c122b901de224348ce0ba795a7c22741fa39
conn.close()
