import sqlite3

# Ruta a tu base de datos
db_path = 'C:\\Users\\Tecno\\Desktop\\Proyecto-AESTETHIC\\instance\\Aestethic.db'

# Conexión a la base de datos
conn = sqlite3.connect(db_path)  # Reemplaza con la ruta a tu archivo de base de datos si es necesario
cursor = conn.cursor()

horarios = [
    # Tratamientos Corporales
    (1, 'Lunes', '09:00', '10:00'),
    (1, 'Jueves', '10:00', '11:00'),
    (2, 'Lunes', '16:00', '17:00'),
    (2, 'Jueves', '17:00', '18:00'),
    (3, 'Martes', '10:00', '11:00'),
    (3, 'Viernes', '15:00', '16:00'),
    (4, 'Martes', '16:00', '17:00'),
    (4, 'Viernes', '17:00', '18:00'),

    # Tratamientos Faciales
    (5, 'Lunes', '10:00', '11:00'),
    (5, 'Jueves', '11:00', '12:00'),
    (7, 'Lunes', '17:00', '18:00'),
    (7, 'Viernes', '09:00', '10:00'),
    (6, 'Martes', '11:00', '12:00'),
    (6, 'Viernes', '15:00', '16:00'),
    (8, 'Martes', '17:00', '18:00'),
    (8, 'Sábado', '09:00', '10:00'),

    # Depilación
    (9, 'Lunes', '11:00', '12:00'),
    (9, 'Jueves', '15:00', '16:00'),
    (11, 'Miércoles', '10:00', '11:00'),
    (11, 'Viernes', '11:00', '12:00'),
    (10, 'Martes', '09:00', '10:00'),
    (10, 'Viernes', '10:00', '11:00'),
    (12, 'Miércoles', '11:00', '12:00'),
    (12, 'Sábado', '11:00', '12:00'),

    # Spa de Manos
    (13, 'Miércoles', '11:00', '12:00'),
    (13, 'Sábado', '15:00', '16:00'),
    (14, 'Miércoles', '15:00', '16:00'),
    (14, 'Sábado', '16:00', '17:00'),
    (15, 'Miércoles', '16:00', '17:00'),
    (15, 'Sábado', '17:00', '18:00'),
    (16, 'Miércoles', '17:00', '18:00'),
    (16, 'Viernes', '11:00', '12:00'),

    # Masajes
    (17, 'Lunes', '15:00', '16:00'),
    (17, 'Jueves', '16:00', '17:00'),
    (18, 'Martes', '10:00', '11:00'),
    (18, 'Viernes', '11:00', '12:00'),
    (19, 'Martes', '15:00', '16:00'),
    (19, 'Viernes', '16:00', '17:00'),
    (20, 'Jueves', '09:00', '10:00'),
    (20, 'Sábado', '17:00', '18:00')
]

# Inserción de los registros en la tabla "horarios"
insert_query = "INSERT INTO horarios (servicio_id, dia_semana, hora_inicio, hora_fin) VALUES (?, ?, ?, ?)"
cursor.executemany(insert_query, horarios)

# Confirmar los cambios
conn.commit()
print("Todos los horarios han sido insertados correctamente en la tabla 'horarios'.")

# Cerrar la conexión
conn.close()
