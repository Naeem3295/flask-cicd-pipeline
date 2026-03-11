import pytest
from app import app

ে
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'success'
    assert data['developer'] == 'MD ABU NAEEM'
    print("✅ Home test passed!")


def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'
    print("✅ Health test passed!")


def test_info(client):
    response = client.get('/api/info')
    assert response.status_code == 200
    data = response.get_json()
    assert 'tech_stack' in data
    assert 'pipeline_stages' in data
    print("✅ Info test passed!")
