from app import db


class Student(db.Model):
    __tablename__ = "student"

    uuid = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    surname = db.Column(db.String(120), nullable=False)
    specialization = db.Column(db.String(120), nullable=False)

    # def __init__(self, uuid, name, surname, specialization):
    #     self.uuid = uuid
    #     self.name = name
    #     self.surname = surname
    #     self.specialization = specialization
