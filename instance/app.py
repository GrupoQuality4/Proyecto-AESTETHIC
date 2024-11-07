import sqlite3

# Ruta a tu archivo de base de datos SQLite
db_path = 'C:\\Users\\Flia Caro Sosa Veron\\OneDrive\\Desktop\\Proyecto-AESTETHIC\\instance\\Aestethic.db'
conn = sqlite3.connect('Aestethic.db')
cursor = conn.cursor()
# Mapeo de días y servicios a IDs correspondientes
# Asumimos que ya tienes los nombres y los IDs correspondientes en las tablas
dias = {
    "Lunes": 1,
    "Martes": 2,
    "Miércoles": 3,
    "Jueves": 4,
    "Viernes": 5,
    "Sábado": 6
}

# Mapeo de servicios a IDs (este es un ejemplo, reemplaza los nombres con los IDs reales de tus servicios)
servicios = {
    "Exfoliación Corporal": 1,
    "Limpieza Facial Profunda": 2,
    "Depilación con Cera": 3,
    "Masaje Relajante con Aromaterapia": 4,
    "Envoltura de Algas o Barro": 5,
    "Peeling Químico": 6,
    "Depilación Láser": 7,
    "Masaje Descontracturante": 8,
    "Microdermoabrasión": 9,
    "Masaje con Piedras Calientes": 10,
    "Tratamiento de Drenaje Linfático": 11,
    "Tratamiento con Ácido Hialurónico": 12,
    "Reflexología": 13,
    "Depilación con Crema Depilatoria": 14,
    "Exfoliación e Hidratación Profunda de Manos": 15,
    "Masaje de Manos": 16,
    "Tratamiento de Parafina": 17,
    "Manicura Completa": 18,
    "Masaje de Reflexología de Pies": 19,
    "Tratamiento Facial Antiedad": 20
}

# Mapeo de bloques de horas (asume que ya tienes estos bloques en la tabla `bloques_horas`)
bloques_horas = {
    ("09:00", "10:00"): 1,
    ("10:00", "11:00"): 2,
    ("11:00", "12:00"): 3,
    ("15:00", "16:00"): 4,
    ("16:00", "17:00"): 5,
    ("17:00", "18:00"): 6
}

# Definir los horarios para cada servicio y día específico
horarios_por_servicio = [
    ("Exfoliación Corporal", "Lunes", "09:00", "10:00"),
    ("Exfoliación Corporal", "Jueves", "10:00", "11:00"),
    ("Limpieza Facial Profunda", "Lunes", "10:00", "11:00"),
    ("Limpieza Facial Profunda", "Jueves", "11:00", "12:00"),
    ("Depilación con Cera", "Lunes", "11:00", "12:00"),
    ("Depilación con Cera", "Jueves", "15:00", "16:00"),
    ("Masaje Relajante con Aromaterapia", "Lunes", "15:00", "16:00"),
    ("Masaje Relajante con Aromaterapia", "Jueves", "16:00", "17:00"),
    ("Envoltura de Algas o Barro", "Lunes", "16:00", "17:00"),
    ("Envoltura de Algas o Barro", "Jueves", "17:00", "18:00"),
    ("Peeling Químico", "Lunes", "17:00", "18:00"),
    ("Peeling Químico", "Viernes", "09:00", "10:00"),
    ("Depilación Láser", "Martes", "09:00", "10:00"),
    ("Depilación Láser", "Viernes", "10:00", "11:00"),
    ("Masaje Descontracturante", "Martes", "10:00", "11:00"),
    ("Masaje Descontracturante", "Viernes", "11:00", "12:00"),
    ("Microdermoabrasión", "Martes", "11:00", "12:00"),
    ("Microdermoabrasión", "Viernes", "15:00", "16:00"),
    ("Masaje con Piedras Calientes", "Martes", "15:00", "16:00"),
    ("Masaje con Piedras Calientes", "Viernes", "16:00", "17:00"),
    ("Tratamiento de Drenaje Linfático", "Martes", "16:00", "17:00"),
    ("Tratamiento de Drenaje Linfático", "Viernes", "17:00", "18:00"),
    ("Tratamiento con Ácido Hialurónico", "Martes", "17:00", "18:00"),
    ("Reflexología", "Sábado", "09:00", "10:00"),
    ("Reflexología", "Miércoles", "09:00", "10:00"),
    ("Depilación con Crema Depilatoria", "Miércoles", "10:00", "11:00"),
    ("Depilación con Crema Depilatoria", "Sábado", "11:00", "12:00"),
    ("Exfoliación e Hidratación Profunda de Manos", "Miércoles", "11:00", "12:00"),
    ("Exfoliación e Hidratación Profunda de Manos", "Sábado", "15:00", "16:00"),
    ("Masaje de Manos", "Miércoles", "15:00", "16:00"),
    ("Masaje de Manos", "Sábado", "16:00", "17:00"),
    ("Tratamiento de Parafina", "Miércoles", "16:00", "17:00"),
    ("Tratamiento de Parafina", "Sábado", "17:00", "18:00"),
    ("Manicura Completa", "Miércoles", "17:00", "18:00"),
    ("Masaje de Reflexología de Pies", "Jueves", "09:00", "10:00"),
    ("Masaje de Reflexología de Pies", "Sábado", "17:00", "18:00"),
    ("Tratamiento Facial Antiedad", "Miércoles", "15:00", "16:00"),
    ("Tratamiento Facial Antiedad", "Viernes", "17:00", "18:00")
]

# Insertar los horarios en la tabla `horarios`
for servicio, dia, hora_inicio, hora_fin in horarios_por_servicio:
    servicio_id = servicios[servicio]
    dia_id = dias[dia]
    bloque_hora_id = bloques_horas[(hora_inicio, hora_fin)]
    cursor.execute('INSERT INTO horarios (servicio_id, dia_id, bloque_hora_id) VALUES (?, ?, ?)',
                   (servicio_id, dia_id, bloque_hora_id))

# Confirmar los cambios y cerrar la conexión
conn.commit()
conn.close()

print("Horarios insertados correctamente en la base de datos.")

