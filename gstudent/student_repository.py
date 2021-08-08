# from gstudent.api import api


class StudentRepository:
    @staticmethod
    def get_students_list(params):
        from gstudent.models import Student
        params = {k: v for k, v in params.items() if v}
        students = Student.query.filter_by(**params).all()
        return students

    @staticmethod
    def create_user(data):
        import uuid
        from app import db
        from gstudent.models import Student
        uuid = uuid.uuid4()
        name = data["name"]
        surname = data["surname"]
        specialization = data["specialization"]
        student = Student(uuid=str(uuid), name=name, surname=surname, specialization=specialization)
        db.session.add(student)
        db.session.commit()
        return student

    @staticmethod
    def get_student_by_uuid(uuid):
        from gstudent.models import Student
        from gstudent.api import api
        student = Student.query.filter_by(uuid=uuid).one_or_none()
        if student:
            return student
        api.abort(404, f"Student {uuid} doesn't exist")

    @staticmethod
    def update_student(uuid, data):
        from app import db
        from gstudent.models import Student
        student = Student.query.filter_by(uuid=uuid).first()
        student.name = data["name"]
        student.surname = data["surname"]
        student.specialization = data["specialization"]
        db.session.commit()
        return student

    @staticmethod
    def delete_student(uuid):
        from app import db
        from gstudent.models import Student
        student = Student.query.filter_by(uuid=uuid).first()
        if student:
            db.session.delete(student)
            db.session.commit()
