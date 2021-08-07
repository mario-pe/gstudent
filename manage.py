import os
import sqlite3

from flask import Flask
from flask.cli import FlaskGroup
from flask_sqlalchemy import SQLAlchemy

from app import app, db
from gstudent.models import Student

cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

def create_test_db(app):
    if app.config["SQLALCHEMY_DATABASE_URI"] == f"sqlite:///{os.getcwd()}/test.db":
        db.drop_all()
        db.create_all()
        db.session.commit()

@cli.command("seed_db")
def seed_db():
    db.session.add(Student(uuid="6dec67e7-626a-40cc-b715-b445e703adbb", name="michael", surname="mherman", specialization="math"))
    db.session.commit()
    print("Student added")




if __name__ == "__main__":
    cli()
