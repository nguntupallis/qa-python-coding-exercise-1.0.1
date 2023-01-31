from contextlib import contextmanager
import pytest
from pytest_bdd import scenario, given, when, then
from requests.models import Response
import requests
from json import loads
import os

import tests.constants as constants
from tests.utilities.helpers.apiClient import apiClient

@scenario('../features/versionEndpoint.feature', 'Check Status Code')
def test_status_code():
    print("\nTest status code")

@pytest.fixture
def version_shared_data():
    baseUrl = constants.URL + "/" + constants.VERSIONENDPOINT
    request = ""
    response = Response()

    return [baseUrl, request, response]

@given("I have the endpoint - version")
def given_i_have_the_endpoint(version_shared_data):
    baseUrl, request, response = version_shared_data    

@when("I make the <requestType> request")
def when_i_make_the_request(requestType, version_shared_data):
    baseUrl, request, response = version_shared_data   
    version_shared_data[1] = requestType
    version_shared_data[2] = requests.request(requestType, baseUrl)

@then("the request should return <status> status")
def then_the_request_should_return_status(status, version_shared_data):
    baseUrl, request, response = version_shared_data   
    assert response.status_code == int(status), 'For {} request, Expected {} but {} was returned'.format(request.upper(), status, response.status_code)

@scenario('../features/versionEndpoint.feature', 'Check get version response body')
def test_response_body(version_shared_data):
    baseUrl, request, response = version_shared_data   
    print("\nTest response body")

@given('the user sends a GET request to the version endpoint')
def given_get_version_request(version_shared_data):
    baseUrl, request, response = version_shared_data   
    version_shared_data[2] = requests.get(baseUrl)

@when('the server receives the request')
def server_receives_request():
    pass

@then('it returns a response body <responseBody>')
def check_response_body(responseBody, version_shared_data):
    baseUrl, request, response = version_shared_data   
    with open(os.path.join('responseBodies', responseBody)) as f:
        expected_response = loads(f.read())
    assert response.json() == expected_response, 'Expected {} but {} was returned'.format(expected_response, response.json())
    
    
@scenario('../features/versionEndpoint.feature', 'Check non-get version response body')
def test_response_body():
    print("\nTest response body")

@given('the user sends a <requestType> request to the version endpoint')
def given_non_get_version_request(requestType, version_shared_data):
    baseUrl, request, response = version_shared_data   
    version_shared_data[2] = requests.request(requestType, baseUrl)