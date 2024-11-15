import pytest
from app import app

@pytest.fixture
def client():
    # Set up a test client for the Flask app
    with app.test_client() as client:
        yield client

def test_home_page(client):
    # Test if the home page loads correctly
    response = client.get('/')
    assert response.status_code == 200
    assert b"Task List" in response.data

def test_add_task(client):
    # Test adding a task
    response = client.post('/add', data={'task': 'Test Task'})
    assert response.status_code == 405  # Redirect to home page

    # Verify the task was added
    response = client.get('/')
    assert b"Test Task" in response.data

def test_delete_task(client):
    # Add a task first
    client.post('/add', data={'task': 'Task to Delete'})

    # Verify task is present
    response = client.get('/')
    assert b'Task to Delete' in response.data

    # Delete the task
    response = client.get('/delete/0')
    assert response.status_code == 302  # Redirect to home page

    # Verify the task was deleted
    response = client.get('/')
    print(response.data)
    assert b"Task to Delete" not in response.data
