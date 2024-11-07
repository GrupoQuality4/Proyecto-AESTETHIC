import sqlite3

# Conectar a la base de datos
db_path = 'C:\\Users\\Tecno\\Desktop\\Proyecto-AESTETHIC\\instance\\Aestethic.db'
connection = sqlite3.connect(db_path)
cursor = connection.cursor()

try:
    # Paso 1: Eliminar todos los registros de la tabla 'reservas'
    cursor.execute("DELETE FROM reservas;")

    # Paso 2: Añadir la columna 'hora_turno' a la tabla 'reservas'
    cursor.execute("ALTER TABLE reservas ADD COLUMN hora_turno TIME;")

    # Confirmar los cambios
    connection.commit()
    print("Registros eliminados y columna 'hora_turno' añadida exitosamente.")

except Exception as e:
    print("Ocurrió un error:", e)

finally:
    # Cerrar la conexión a la base de datos
    connection.close()

