from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from gstudent.api import api


def create_app(config_path):
    # pass
    app = Flask(__name__)
    app.config.from_object(config_path)
    db = SQLAlchemy()
    db.init_app(app)
    api.init_app(app)
    return app, db
