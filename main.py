from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix
from flask_sqlalchemy import SQLAlchemy

from gstudent import api

app = Flask(__name__)

db = SQLAlchemy(app)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://postgres:postgres@localhost:5432/student"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
api.init_app(app)
db.create_all()
app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == "__main__":
    app.run(debug=True)
