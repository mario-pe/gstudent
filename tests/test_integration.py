import os
import tempfile

import factory
import ipdb
import pytest

from app import db
from run import create_app
from manage import create_db, create_test_db
from tests.factories import StudentFactory


@pytest.fixture
def client():
    """Creating test application"""
    # _, db_path = tempfile.mkstemp()
    app, db = create_app("test_settings")
    with app.test_client() as client:
        with app.app_context():
            create_test_db(app)
        yield client
    db.close_all_sessions()
    return app


def test_should_return_empty_list_if_students_not_exists(client):
    re = client.get("/students/")
    assert re.status_code == 200
    assert re.json == []


def tests_should_return_status_code_200_and_list_of_students(client):
    number_of_expected_students = 5
    StudentFactory.create_batch(number_of_expected_students)

    re = client.get("/students/")

    assert re.status_code == 200
    assert len(re.json) == number_of_expected_students


def test_should_create_student_and_return_status_code_201(client):
    student_data = factory.build(dict, FACTORY_CLASS=StudentFactory)
    student_data.pop("uuid")

    re = client.post("/students/", json=student_data, headers={'content-type': 'application/json'})

    assert re.status_code == 201
    assert re.json["name"] == student_data["name"]
    assert re.json["surname"] == student_data["surname"]
    assert re.json["specialization"] == student_data["specialization"]

# def test_should_return_400_if_name_is_integer(client):
#     student_data = factory.build(dict, FACTORY_CLASS=StudentFactory)
#     student_data.pop("uuid")
#     student_data["name"] = 1
#
#     re = client.post("/students/", json=student_data, headers={'content-type': 'application/json'})
#
#     assert re.status_code == 400
#
# def test_should_return_404_if_student_with_desired_uuid_not_exists(client):
#     pass