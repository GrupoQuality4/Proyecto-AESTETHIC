from . import db

class Dia(db.Model):
    __tablename__ = 'dias'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=True, nullable=False)
    horarios = db.relationship('Horario', back_populates='dia')

    def __repr__(self):
        return f"<Dia {self.nombre}>"