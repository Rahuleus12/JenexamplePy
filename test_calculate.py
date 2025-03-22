import pytest
import json
from calculate import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_add(client):
    response = client.get('/add?a=2&b=3')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['result'] == 5
    
    response = client.get('/add?a=4&b=5')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['result'] == 9

def test_subtract(client):
    response = client.get('/subtract?a=3&b=1')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['result'] == 2
    
    response = client.get('/subtract?a=4&b=5')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['result'] == -1

def test_multiply(client):
    response = client.get('/multiply?a=2&b=3')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['result'] == 6
    
    response = client.get('/multiply?a=4&b=5')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['result'] == 20

def test_divide(client):
    response = client.get('/divide?a=27&b=3')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['result'] == 9.0
    
    response = client.get('/divide?a=42&b=14')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['result'] == 3.0
    
def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Calculator API' in response.data


