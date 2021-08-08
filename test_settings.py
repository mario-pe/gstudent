import os
import sqlite3

TESTING = True
# SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost:5432/student_test"
#
SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.getcwd()}/test.db"
SQLALCHEMY_TRACK_MODIFICATIONS = False
RESTX_VALIDATE = True
