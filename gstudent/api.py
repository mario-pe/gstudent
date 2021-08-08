from flask_restx import Api

from gstudent.views import ns as student_api

api = Api(title="student_api", verison="0.1", description="Student manager")
api.add_namespace(student_api)
