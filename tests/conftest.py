import pytest
import requests
import helpers
from constants.urls_constants import UrlsConstants


@pytest.fixture
def user_data_and_token():
    payload = helpers.payload
    response = requests.post(UrlsConstants.CREATE_USER, data=payload)
    token = response.json()['accessToken']

    yield payload, response, token

    requests.delete(UrlsConstants.DELETE_USER, headers={'Authorization': token})
