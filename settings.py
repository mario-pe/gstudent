import os

os.putenv("FLASK_ENV", "development")
SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:postgres@db:5432/student"
SQLALCHEMY_TRACK_MODIFICATIONS = False
RESTX_VALIDATE = True
