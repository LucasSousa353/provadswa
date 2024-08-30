from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Disciplina(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    semester = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'<Disciplina {self.name}>'
