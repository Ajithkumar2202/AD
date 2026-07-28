from API.index import app


def test_app_imports():
    client = app.test_client()
    response = client.get('/api/get_location')
    assert response.status_code == 200
