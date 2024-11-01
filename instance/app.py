import sqlite3

db_path = 'C:\\Users\\Tecno\\Desktop\\\\Proyecto-AESTETHIC\\instance\\Aestethic.db'
#db_path = 'C:\\Users\\Flia Caro Sosa Veron\\OneDrive\\Desktop\\Proyecto-AESTETHIC\\instance\\Aestethic.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

horarios = [
    # Exfoliación Corporal
    ("Exfoliación Corporal", "Lunes", "09:00", "10:00"),
    ("Exfoliación Corporal", "Jueves", "10:00", "11:00"),
    # Limpieza Facial Profunda
    ("Limpieza Facial Profunda", "Lunes", "10:00", "11:00"),
    ("Limpieza Facial Profunda", "Jueves", "11:00", "12:00"),
    # Depilación con Cera
    ("Depilación con Cera", "Lunes", "11:00", "12:00"),
    ("Depilación con Cera", "Jueves", "15:00", "16:00"),
    # Masaje Relajante con Aromaterapia
    ("Masaje Relajante con Aromaterapia", "Lunes", "15:00", "16:00"),
    ("Masaje Relajante con Aromaterapia", "Jueves", "16:00", "17:00"),
    # Envoltura de Algas o Barro
    ("Envoltura de Algas o Barro", "Lunes", "16:00", "17:00"),
    ("Envoltura de Algas o Barro", "Jueves", "17:00", "18:00"),
    # Peeling Químico
    ("Peeling Químico", "Lunes", "17:00", "18:00"),
    ("Peeling Químico", "Viernes", "09:00", "10:00"),
    # Depilación Láser
    ("Depilación Láser", "Martes", "09:00", "10:00"),
    ("Depilación Láser", "Viernes", "10:00", "11:00"),
    # Masaje Descontracturante
    ("Masaje Descontracturante", "Martes", "10:00", "11:00"),
    ("Masaje Descontracturante", "Viernes", "11:00", "12:00"),
    # Microdermoabrasión
    ("Microdermoabrasión", "Martes", "11:00", "12:00"),
    ("Microdermoabrasión", "Viernes", "15:00", "16:00"),
    # Masaje con Piedras Calientes
    ("Masaje con Piedras Calientes", "Martes", "15:00", "16:00"),
    ("Masaje con Piedras Calientes", "Viernes", "16:00", "17:00"),
    # Tratamiento de Drenaje Linfático
    ("Tratamiento de Drenaje Linfático", "Martes", "16:00", "17:00"),
    ("Tratamiento de Drenaje Linfático", "Viernes", "17:00", "18:00"),
    # Tratamiento con Ácido Hialurónico
    ("Tratamiento con Ácido Hialurónico", "Martes", "17:00", "18:00"),
    ("Tratamiento con Ácido Hialurónico", "Sábado", "09:00", "10:00"),
    # Reflexología
    ("Reflexología", "Miércoles", "09:00", "10:00"),
    ("Reflexología", "Sábado", "10:00", "11:00"),
    # Depilación con Crema Depilatoria
    ("Depilación con Crema Depilatoria", "Miércoles", "10:00", "11:00"),
    ("Depilación con Crema Depilatoria", "Sábado", "11:00", "12:00"),
    # Exfoliación e Hidratación Profunda de Manos
    ("Exfoliación e Hidratación Profunda de Manos", "Miércoles", "11:00", "12:00"),
    ("Exfoliación e Hidratación Profunda de Manos", "Sábado", "15:00", "16:00"),
    # Masaje de Manos
    ("Masaje de Manos", "Miércoles", "15:00", "16:00"),
    ("Masaje de Manos", "Sábado", "16:00", "17:00"),
    # Tratamiento de Parafina
    ("Tratamiento de Parafina", "Miércoles", "16:00", "17:00"),
    ("Tratamiento de Parafina", "Sábado", "17:00", "18:00"),
    # Manicura Completa
    ("Manicura Completa", "Miércoles", "17:00", "18:00"),
    ("Manicura Completa", "Viernes", "11:00", "12:00"),
    # Masaje de Reflexología de Pies
    ("Masaje de Reflexología de Pies", "Jueves", "09:00", "10:00"),
    ("Masaje de Reflexología de Pies", "Sábado", "17:00", "18:00")
]

# Insertar los horarios en la tabla `horarios`
for servicio, dia_semana, hora_inicio, hora_fin in horarios:
    # Obtener el ID del servicio (asegúrate de que los servicios ya están en la tabla `servicios`)
    cursor.execute("SELECT id FROM servicio WHERE nombre = ?", (servicio,))
    result = cursor.fetchone()
    if result:
        servicio_id = result[0]
        
        # Insertar horario en la tabla `horarios`
        cursor.execute('''
            INSERT INTO horarios (servicio_id, dia_semana, hora_inicio, hora_fin)
            VALUES (?, ?, ?, ?)
        ''', (servicio_id, dia_semana, hora_inicio, hora_fin))

print("Horarios de disponibilidad insertados correctamente.")
conn.commit()
conn.close()