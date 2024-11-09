import sqlite3

<<<<<<< HEAD
def eliminar_reserva(id_reserva):
    # Ruta a tu base de datos
    db_path = 'C:\\Users\\Flia Caro Sosa Veron\\OneDrive\\Desktop\\Proyecto-AESTETHIC\\instance\\Aestethic.db'
    
    # Conexión a la base de datos
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Consulta para eliminar el registro con el id especificado
    cursor.execute("DELETE FROM reservas WHERE id = ?", (id_reserva,))
    
    # Confirmar cambios
    conn.commit()
    conn.close()
    print(f"Registro con id {id_reserva} eliminado exitosamente.")

# Llamada a la función con un id específico
eliminar_reserva(26)  # Cambia '1' por el id que quieras eliminar
=======
# Ruta a tu base de datos
db_path = 'C:\\Users\\Flia Caro Sosa Veron\\OneDrive\\Desktop\\Proyecto-AESTETHIC\\instance\\Aestethic.db'

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

>>>>>>> 2638eb38c51dd15f3e5c09ec5d38bac89e618520
