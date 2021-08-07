from flask_restx import Namespace, Resource, fields, reqparse
from flask_restx._http import HTTPStatus

from gstudent.studentrepository import StudentRepository

parser = reqparse.RequestParser()
parser.add_argument('name', location='args')
parser.add_argument('surname', location='args')
parser.add_argument('specialization', location='args')

ns = Namespace('students', description='students operations')

student = ns.model(
    "Student",{
        "uuid": fields.String(required=True, pattern="^[0-9A-F]{8}-[0-9A-F]{4}-4[0-9A-F]{3}-[89AB][0-9A-F]{3}-[0-9A-F]{12}$",description="The student identifier"),
        "name": fields.String(required=True, description="The student name"),
        "surname": fields.String(required=True, description="The student surname"),
        "specialization": fields.String(required=True, description="The student specialization"),
    }

)



@ns.route('/')
class StudentList(Resource):
    '''Shows a list of all students, and lets you POST to add new student'''
    @ns.doc('list_students')
    @ns.marshal_list_with(student)
    def get(self, **kwargs):
        '''List all students'''
        args = parser.parse_args()
        students = StudentRepository.get_students_list(args)
        return students

    @ns.doc('create_student')
    @ns.marshal_list_with(student)
    def post(self):
        '''Create a new student'''
        student = StudentRepository.create_user(ns.payload)
        return student, 201


@ns.route('/<string:uuid>')
@ns.response(HTTPStatus.NOT_FOUND, HTTPStatus.NOT_FOUND.description)
@ns.response(HTTPStatus.BAD_REQUEST, HTTPStatus.BAD_REQUEST.description)
@ns.param('uuid', 'The student identifier')
class StudentDetails(Resource):
    @ns.doc('get_student_by_uuid')
    @ns.response(HTTPStatus.OK, HTTPStatus.OK.description)
    @ns.response(HTTPStatus.NOT_FOUND, HTTPStatus.NOT_FOUND.description)
    @ns.marshal_with(student)
    def get(self, uuid):
        return StudentRepository.get_student_by_uuid(uuid)

    @ns.doc('update_student_by_uuid')
    @ns.marshal_with(student, code=400)
    def put(self, uuid):
        student = StudentRepository.update_student(uuid, ns.payload)
        return student

    @ns.doc('delete_student_by_uuid')
    @ns.response(200, 'Student deleted')
    def delete(self, uuid):
        StudentRepository.delete_student(uuid)
        return "", 200
