import os
import tempfile

import pytest

from api.api import create_app
from api.resources.emailTracking import EmailTracking


endpoint = '/email'

@pytest.fixture
def client():
    app = create_app({'TESTING': True})

    with app.test_client() as client:
        yield client

def test_successful_request(client):

    ticket = {
        "id": 1,
        "created_at": "2021-06-14T08:53:30Z",
        "subject": "Berichtgeving Support Case: 99999",
        "body": "Lorem 3STUHB466811858 Ipsum"
    }

    response = client.post(endpoint, json=ticket)

    assert response.content_type == 'application/json'
    assert response.status_code == 200
    assert response.json == {
        "parcel_id": 79271088,
        "weight": 0.2,
        "tracking_number": "3STUHB466811858",
        "announced_at": "2021-01-11 15:27:45",
        "shipping_country_id": 2,
        "carrier_code": "postnl"
    }

def test_request_not_json(client):
    ticket = {
        "id": 1,
        "created_at": "2021-06-14T08:53:30Z",
        "subject": "Berichtgeving Support Case: 99999",
        "body": "Lorem 3STUHB466811858 Ipsum"
    }

    response = client.post(endpoint, data=ticket)

    assert response.content_type == 'application/json'
    assert response.status_code == 400
    assert response.json == 'Failed Parsing input. Accepts JSON.'

def test_invalid_email_json(client):
    ticket = {
        "id": 1,
        "created_at": "2021-06-14T08:53:30Z",
        "body": "Lorem 3STUHB466811858 Ipsum"
    }

    response = client.post(endpoint, json=ticket)

    assert response.content_type == 'application/json'
    assert response.status_code == 400
    assert response.json == "Failed Parsing JSON. 'subject' and 'body' keys are required."

def test_no_tracking_number(client):
    ticket = {
        "id": 1,
        "created_at": "2021-06-14T08:53:30Z",
        "subject": "Berichtgeving Support Case: 99999",
        "body": "Lorem Ipsum"
    }

    response = client.post(endpoint, json=ticket)

    assert response.content_type == 'application/json'
    assert response.status_code == 400
    assert response.json == 'No valid tracking number found in email.'

def test_no_dataset_match(client):
    ticket = {
        "id": 1,
        "created_at": "2021-06-14T08:53:30Z",
        "subject": "Berichtgeving Support Case: 99999",
        "body": "Lorem 3SXBTA3091265 Ipsum"
    }

    response = client.post(endpoint, json=ticket)

    assert response.content_type == 'application/json'
    assert response.status_code == 400
    assert response.json == 'No parcel found with tracking number: 3SXBTA3091265'

def test_invalid_request_method(client):
    response = client.get(endpoint)

    assert response.content_type == 'application/json'
    assert response.status_code == 405
    assert response.json == {
        "message": "The method is not allowed for the requested URL."
    }
