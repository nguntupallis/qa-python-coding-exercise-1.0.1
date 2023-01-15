import pytest
from pytest_bdd import scenario, given, when, then
from requests.models import Response
import requests
from json import loads
import os
import tests.requestBodies.buildProductRequestBody as buildProductRequestBody
import tests.constants as constants
from tests.utilities.helpers.apiClient import apiClient

@scenario('../features/jsonEndpoint.feature', 'Check Status Code')
def test_status_code():
    print("\nTest status code")

pytest.apiUrl = constants.URL
pytest.jsonendpoint = constants.JSONENDPOINT
pytest.response = Response()

@given("I have the endpoint - json")
def given_i_have_the_endpoint():
    pytest.base_url = pytest.apiUrl + "/" + pytest.jsonendpoint

@when("I make the <requestType> request")
def when_i_make_the_request(requestType):
    if (requestType == "post"):
        requestBody = buildProductRequestBody.buildRequest("SAVINGS", "SAVINGS", 1.1)
        pytest.response = requests.post(pytest.base_url, data=requestBody)        
    else:
        pytest.response = requests.request(requestType, pytest.base_url)

@then("the request should return <status> status")
def then_the_request_should_return_status(status):
    response = pytest.response
    assert response.status_code == int(status)

# @scenario('../features/versionEndpoint.feature', 'Check get version response body')
# def test_response_body():
#     print("\nTest response body")

# @given('the user sends a GET request to the version endpoint')
# def given_get_version_request():
#     base_url = pytest.apiUrl + "/" + pytest.endpoint
#     pytest.response = requests.get(base_url)

# @when('the server receives the request')
# def server_receives_request():
#     pass

# @then('it returns a response body <responseBody>')
# def check_response_body(responseBody):
#     with open(os.path.join('responseBodies', responseBody)) as f:
#         expected_response = loads(f.read())
#     assert pytest.response.json() == expected_response
    
    
# @scenario('../features/versionEndpoint.feature', 'Check non-get version response body')
# def test_response_body():
#     print("\nTest response body")

# @given('the user sends a <requestType> request to the version endpoint')
# def given_non_get_version_request(requestType):
#     base_url = pytest.apiUrl + "/" + pytest.endpoint
#     pytest.response = requests.request(requestType, base_url)