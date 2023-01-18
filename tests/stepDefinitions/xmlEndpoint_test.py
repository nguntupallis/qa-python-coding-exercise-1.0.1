import pytest
from pytest_bdd import scenario, given, when, then
from requests.models import Response
import requests
from json import loads
import os

import tests.constants as constants
from tests.utilities.helpers.apiClient import apiClient

@scenario('../features/xmlEndpoint.feature', 'Check Status Code')
def test_status_code():
    print("\nTest status code")

pytest.apiUrl = constants.URL
pytest.xmlEndpoint = constants.XMLENDPOINT
pytest.response = Response()

@given("I have the endpoint - xml")
def given_i_have_the_endpoint():
    pytest.base_url = pytest.apiUrl + "/" + pytest.xmlEndpoint

@when("I make the <requestType> request")
def when_i_make_the_request(requestType):
    pytest.response = requests.request(requestType, pytest.base_url)

@then("the request should return <status> status")
def then_the_request_should_return_status(status):
    response = pytest.response
    assert response.status_code == int(status), 'Expected {} but {} was returned'.format(status, response.status_code)

# @scenario('../features/xmlEndpoint.feature', 'Check get version response body')
# def test_response_body():
#     print("\nTest response body")

# @given('the user sends a GET request to the version endpoint')
# def given_get_version_request():
#     pytest.response = requests.get(pytest.base_url)

# @when('the server receives the request')
# def server_receives_request():
#     pass

# @then('it returns a response body <responseBody>')
# def check_response_body(responseBody):
#     with open(os.path.join('responseBodies', responseBody)) as f:
#         expected_response = loads(f.read())
#     assert pytest.response.json() == expected_response, 'Expected {} but {} was returned'.format(expected_response, pytest.response.json())
    
    
# @scenario('../features/xmlEndpoint.feature', 'Check non-get version response body')
# def test_response_body():
#     print("\nTest response body")

# @given('the user sends a <requestType> request to the version endpoint')
# def given_non_get_version_request(requestType):
#     pytest.response = requests.request(requestType, pytest.base_url)