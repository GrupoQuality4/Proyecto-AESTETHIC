from sqlalchemy.orm import relationship
from . import db

class Reserva(db.Model):
    __tablename__ = 'reservas'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    servicio = db.Column(db.String(255))
    fecha_reserva = db.Column(db.Date)
    fecha_uso = db.Column(db.Date)
    nombre_cliente = db.Column(db.String(255))
    hora_turno = db.Column(db.String(10))  # Nueva columna para almacenar la hora del turno

    user = relationship("User", back_populates="reservas")
    
    def __init__(self, user_id, servicio, fecha_reserva, fecha_uso, nombre_cliente, hora_turno):
        self.user_id = user_id
        self.servicio = servicio
        self.fecha_reserva = fecha_reserva
        self.fecha_uso = fecha_uso
        self.nombre_cliente = nombre_cliente
        self.hora_turno = hora_turno  # Inicialización de hora_turno




