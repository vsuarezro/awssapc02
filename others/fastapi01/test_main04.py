from fastapi.testclient import TestClient
from .main04 import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_read_item():
    response = client.get("/items/name1", headers={"X-Token": "mysupersecrettoken"})
    assert response.status_code == 200
    assert response.json() == {
        "name": "name1",
        "description": "description of the name1",
        "price": 100.0,
        "tax": 10.0,
    }


def test_read_item_bad_token():
    response = client.get("/items/name1", headers={"X-Token": "IamABadToken"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid X-Token header"}


def test_create_item():
    response = client.post(
        "/items/",
        headers={"X-Token": "mysupersecrettoken"},
        json={
            "name": "name3",
            "description": "description of the name3",
            "price": 200.0,
            "tax": 20.0,
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "name": "name3",
        "description": "description of the name3",
        "price": 200.0,
        "tax": 20.0,
    }
