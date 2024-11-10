import sqlite3

# Ruta a tu base de datos
db_path = 'C:\\Users\\Tecno\\Desktop\\Proyecto-AESTETHIC\\instance\\Aestethic.db'
#db_path = 'C:\\Users\\Flia Caro Sosa Veron\\OneDrive\\Desktop\\Proyecto-AESTETHIC\\instance\\Aestethic.db'

# Conectar a la base de datos
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

try:
    # Consulta SQL para eliminar los registros de la tabla 'reservas'
    consulta = "DELETE FROM reservas"

    # Ejecutar la consulta
    cursor.execute(consulta)
    conn.commit()
    print("Registros eliminados correctamente.")

except sqlite3.Error as error:
    print(f"Error al eliminar registros: {error}")

finally:
    if conn:
        cursor.close()
        conn.close()
        print("Conexión cerrada.")

