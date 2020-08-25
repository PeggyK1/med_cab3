from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_valid_input():
    """Return 200 Success when input is valid."""
    response = client.post(
        '/predict',
        json={
            'ailment': 'Depression',
            'effect': 'Happy',
            'flavor': 'Citrus',
            'location': 'Los Angeles, CA'
        }
    )
    body = response.json()
    assert response.status_code == 200
    assert body['prediction'] in [True, False]


def test_invalid_input():
    """Return 422 Validation Error when x1 is negative."""
    response = client.post(
        '/predict',
        json={
            'ailment': 'Depression',
            'effect': 'Happy',
            'flavor': 'Citrus',
            'location': 'Los Angeles, CA'
        }
    )
    body = response.json()
    assert response.status_code == 422
    assert 'ailment' in body['detail'][0]['loc']
