from . import db

class Disponibilidad(db.Model):
    __tablename__ = 'disponibilidad'
    id = db.Column(db.Integer, primary_key=True)
    servicio = db.Column(db.String(100), nullable=False)
    dia_semana = db.Column(db.String(10), nullable=False)
    hora_inicio = db.Column(db.Time, nullable=False)
    hora_fin = db.Column(db.Time, nullable=False)
    total_turnos = db.Column(db.Integer, nullable=False)

    def __init__(self, servicio, dia_semana, hora_inicio, hora_fin, total_turnos):
        self.servicio = servicio
        self.dia_semana = dia_semana
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.total_turnos = total_turnos
