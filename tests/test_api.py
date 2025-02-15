import pytest
from fastapi.testclient import TestClient
from app.main import app
import json
from pathlib import Path

client = TestClient(app)

def test_run_operations_task():
    response = client.post("/run", params={"task": "Format the markdown file readme.md"})
    assert response.status_code == 200
    assert "status" in response.json()
    assert response.json()["status"] == "success"

def test_run_business_task():
    response = client.post("/run", params={"task": "Fetch data from https://api.example.com"})
    assert response.status_code == 200
    assert "status" in response.json()
    assert response.json()["status"] == "success"

def test_read_file():
    # Create test file
    Path("./data").mkdir(exist_ok=True)
    test_file = Path("./data/test.txt")
    test_file.write_text("Test content")
    
    response = client.get("/read", params={"path": "test.txt"})
    assert response.status_code == 200
    assert "content" in response.json()
    assert response.json()["content"] == "Test content"

def test_read_file_outside_data():
    response = client.get("/read", params={"path": "../secret.txt"})
    assert response.status_code == 400 