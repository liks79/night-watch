from fastapi import HTTPException
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_redis_health_check():
    response = client.get("/redis/health")
    assert response.status_code == 200
    assert response.json() == {"Hello": "Redis"}


def test_redis_health_check_bad():
    # Write test code for fail case
    pass


def test_postgresql_health_check():
    response = client.get("/postgresql/health")
    assert response.status_code == 200
    assert response.json() == {"Hello": "Postgresql"}


def test_postgresql_health_check_bad():
    # Write test code for fail case
    pass
