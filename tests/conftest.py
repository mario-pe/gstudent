import pytest
from run import create_app
from manage import create_db, create_test_db


@pytest.fixture
def client():
    """Creating test application"""
    app, db = create_app("test_settings")
    with app.test_client() as client:
        with app.app_context():
            create_test_db(app)
        yield client
    db.close_all_sessions()
    return app
