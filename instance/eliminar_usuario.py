import sqlite3

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
conn.close()
