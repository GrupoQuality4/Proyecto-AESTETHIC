import sqlite3

# Datos de disponibilidad de cada servicio
horarios = [
    # Exfoliación Corporal
    ("Exfoliación Corporal", "Lunes", "09:00", "10:00"),
    ("Exfoliación Corporal", "Lunes", "14:00", "15:00"),
    ("Exfoliación Corporal", "Lunes", "17:00", "18:00"),
    ("Exfoliación Corporal", "Miércoles", "09:00", "10:00"),
    ("Exfoliación Corporal", "Miércoles", "17:00", "18:00"),
    ("Exfoliación Corporal", "Miércoles", "20:00", "21:00"),
    ("Exfoliación Corporal", "Jueves", "13:00", "14:00"),
    ("Exfoliación Corporal", "Jueves", "19:00", "20:00"),
    ("Exfoliación Corporal", "Viernes", "09:00", "10:00"),
    ("Exfoliación Corporal", "Viernes", "17:00", "18:00"),
    ("Exfoliación Corporal", "Sábado", "14:00", "15:00"),

    # Limpieza Facial Profunda
    ("Limpieza Facial Profunda", "Lunes", "10:00", "11:00"),
    ("Limpieza Facial Profunda", "Martes", "18:00", "19:00"),
    ("Limpieza Facial Profunda", "Miércoles", "20:00", "21:00"),
    ("Limpieza Facial Profunda", "Viernes", "10:00", "11:00"),
    ("Limpieza Facial Profunda", "Sábado", "16:00", "17:00"),

    # Depilación con Cera
    ("Depilación con Cera", "Lunes", "11:00", "12:00"),
    ("Depilación con Cera", "Viernes", "11:00", "12:00"),

    # Masaje Relajante con Aromaterapia
    ("Masaje Relajante con Aromaterapia", "Lunes", "12:00", "13:00"),
    ("Masaje Relajante con Aromaterapia", "Jueves", "16:00", "17:00"),
    ("Masaje Relajante con Aromaterapia", "Viernes", "12:00", "13:00"),
    ("Masaje Relajante con Aromaterapia", "Sábado", "18:00", "19:00"),

    # Envoltura de Algas o Barro
    ("Envoltura de Algas o Barro", "Martes", "09:00", "10:00"),
    ("Envoltura de Algas o Barro", "Martes", "14:00", "15:00"),
    ("Envoltura de Algas o Barro", "Miércoles", "18:00", "19:00"),
    ("Envoltura de Algas o Barro", "Sábado", "09:00", "10:00"),

    # Peeling Químico
    ("Peeling Químico", "Martes", "10:00", "11:00"),
    ("Peeling Químico", "Martes", "17:00", "18:00"),
    ("Peeling Químico", "Miércoles", "14:00", "15:00"),
    ("Peeling Químico", "Jueves", "17:00", "18:00"),
    ("Peeling Químico", "Sábado", "10:00", "11:00"),

    # Depilación Láser
    ("Depilación Láser", "Martes", "11:00", "12:00"),
    ("Depilación Láser", "Martes", "19:00", "20:00"),
    ("Depilación Láser", "Miércoles", "19:00", "20:00"),
    ("Depilación Láser", "Viernes", "19:00", "20:00"),
    ("Depilación Láser", "Sábado", "11:00", "12:00"),

    # Masaje Descontracturante
    ("Masaje Descontracturante", "Martes", "12:00", "13:00"),
    ("Masaje Descontracturante", "Miércoles", "15:00", "16:00"),
    ("Masaje Descontracturante", "Viernes", "20:00", "21:00"),
    ("Masaje Descontracturante", "Sábado", "12:00", "13:00"),

    # Microdermoabrasión
    ("Microdermoabrasión", "Lunes", "15:00", "16:00"),
    ("Microdermoabrasión", "Martes", "13:00", "14:00"),
    ("Microdermoabrasión", "Martes", "19:00", "20:00"),
    ("Microdermoabrasión", "Miércoles", "10:00", "11:00"),
    ("Microdermoabrasión", "Jueves", "18:00", "19:00"),
    ("Microdermoabrasión", "Sábado", "15:00", "16:00"),

    # Depilación con Hilo
    ("Depilación con Hilo", "Martes", "16:00", "17:00"),
    ("Depilación con Hilo", "Miércoles", "11:00", "12:00"),
    ("Depilación con Hilo", "Jueves", "15:00", "16:00"),

    # Masaje con Piedras Calientes
    ("Masaje con Piedras Calientes", "Lunes", "16:00", "17:00"),
    ("Masaje con Piedras Calientes", "Miércoles", "12:00", "13:00"),
    ("Masaje con Piedras Calientes", "Jueves", "14:00", "15:00"),
    ("Masaje con Piedras Calientes", "Sábado", "20:00", "21:00"),

    # Tratamiento de Drenaje Linfático
    ("Tratamiento de Drenaje Linfático", "Martes", "15:00", "16:00"),
    ("Tratamiento de Drenaje Linfático", "Miércoles", "13:00", "14:00"),
    ("Tratamiento de Drenaje Linfático", "Jueves", "09:00", "10:00"),
    ("Tratamiento de Drenaje Linfático", "Viernes", "14:00", "15:00"),
    ("Tratamiento de Drenaje Linfático", "Sábado", "19:00", "20:00"),

    # Tratamiento con Ácido Hialurónico
    ("Tratamiento con Ácido Hialurónico", "Lunes", "18:00", "19:00"),
    ("Tratamiento con Ácido Hialurónico", "Miércoles", "16:00", "17:00"),
    ("Tratamiento con Ácido Hialurónico", "Jueves", "10:00", "11:00"),
    ("Tratamiento con Ácido Hialurónico", "Jueves", "13:00", "14:00"),
    ("Tratamiento con Ácido Hialurónico", "Viernes", "13:00", "14:00"),
    ("Tratamiento con Ácido Hialurónico", "Viernes", "18:00", "19:00"),

    # Depilación con Crema Depilatoria
    ("Depilación con Crema Depilatoria", "Martes", "20:00", "21:00"),
    ("Depilación con Crema Depilatoria", "Jueves", "11:00", "12:00"),
    ("Depilación con Crema Depilatoria", "Sábado", "17:00", "18:00"),

    # Reflexología
    ("Reflexología", "Miércoles", "17:00", "18:00"),
    ("Reflexología", "Jueves", "12:00", "13:00"),
    ("Reflexología", "Jueves", "20:00", "21:00"),

    # Exfoliación e Hidratación Profunda de Manos
    ("Exfoliación e Hidratación Profunda de Manos", "Lunes", "13:00", "14:00"),
    ("Exfoliación e Hidratación Profunda de Manos", "Miércoles", "15:00", "16:00"),
    ("Exfoliación e Hidratación Profunda de Manos", "Viernes", "16:00", "17:00"),
    ("Exfoliación e Hidratación Profunda de Manos", "Sábado", "09:00", "10:00"),

    # Masaje de Manos
    ("Masaje de Manos", "Martes", "12:00", "13:00"),
    ("Masaje de Manos", "Jueves", "18:00", "19:00"),
    ("Masaje de Manos", "Viernes", "15:00", "16:00"),

    # Tratamiento de Parafina
    ("Tratamiento de Parafina", "Lunes", "17:00", "18:00"),
    ("Tratamiento de Parafina", "Miércoles", "12:00", "13:00"),
    ("Tratamiento de Parafina", "Viernes", "14:00", "15:00"),

    # Manicura Completa
    ("Manicura Completa", "Martes", "09:00", "10:00"),
    ("Manicura Completa", "Jueves", "16:00", "17:00"),
    ("Manicura Completa", "Sábado", "10:00", "11:00"),

    # Masaje de Reflexología de Pies
    ("Masaje de Reflexología de Pies", "Lunes", "20:00", "21:00"),
    ("Masaje de Reflexología de Pies", "Miércoles", "18:00", "19:00"),
    ("Masaje de Reflexología de Pies", "Viernes", "19:00", "20:00"),
]

db_path = 'C:\\Users\\Flia Caro Sosa Veron\\OneDrive\\Desktop\\Proyecto-AESTETHIC\\instance\\Aestethic.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Insertar los datos en la tabla de disponibilidad
for servicio, dia, hora_inicio, hora_fin in horarios:
    cursor.execute('''
        INSERT INTO disponibilidad (servicio, dia_semana, hora_inicio, hora_fin)
        VALUES (?, ?, ?, ?)
    ''', (servicio, dia, hora_inicio, hora_fin))

print("Horarios de disponibilidad insertados correctamente.")
conn.commit()
conn.close()
