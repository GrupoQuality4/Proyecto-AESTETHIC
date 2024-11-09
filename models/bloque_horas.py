from . import db

class BloqueHora(db.Model):
    __tablename__ = 'bloques_horas'
    id = db.Column(db.Integer, primary_key=True)
    hora_inicio = db.Column(db.String(5), nullable=False)
    hora_fin = db.Column(db.String(5), nullable=False)
    horarios = db.relationship('Horario', back_populates='bloque_hora')

    def __repr__(self):
        return f"<BloqueHora {self.hora_inicio} - {self.hora_fin}>"