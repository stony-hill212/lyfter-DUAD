import pytest, sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from app import create_app

@pytest.fixture
def app():
    app=create_app()
    app.config.update({"TESTING": True})
    with app.app_context():
        yield app

@pytest.fixture
def client(app):
    return app.test_client()