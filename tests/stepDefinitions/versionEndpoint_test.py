import pytest
from pytest_bdd import scenario, given, when, then
from requests.models import Response
import requests

import tests.constants as constants
from tests.utilities.helpers.apiClient import apiClient

@scenario('../features/versionEndpoint.feature', 'Check Status Code')
def test_status_code():
    print("\nTest status code")

pytest.apiUrl = constants.URL
pytest.endpoint = constants.VERSIONENDPOINT
pytest.response = Response()

@given("I have the endpoint - version")
def given_i_have_the_endpoint():
    global base_url
    base_url = pytest.apiUrl + "/" + pytest.endpoint

@when("I make the <requestType> request")
def when_i_make_the_request(requestType):
    pytest.response = requests.request(requestType, base_url)

@then("the request should return <status> status")
def then_the_request_should_return_status(status):
    response = pytest.response
    assert response.status_code == int(status)