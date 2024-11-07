from . import db

class Horario(db.Model):
    __tablename__ = 'horarios'
    id = db.Column(db.Integer, primary_key=True)
    servicio_id = db.Column(db.Integer, db.ForeignKey('servicios.id'), nullable=False)
    dia_id = db.Column(db.Integer, db.ForeignKey('dias.id'), nullable=False)
    bloque_hora_id = db.Column(db.Integer, db.ForeignKey('bloques_horas.id'), nullable=False)

    servicio = db.relationship('Servicio', back_populates='horarios')
    dia = db.relationship('Dia', back_populates='horarios')
    bloque_hora = db.relationship('BloqueHora', back_populates='horarios')

    def __repr__(self):
        return f"<Horario Servicio: {self.servicio_id}, Día: {self.dia_id}, Bloque Hora: {self.bloque_hora_id}>"


