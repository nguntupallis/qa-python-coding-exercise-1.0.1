import time
import pytest
from pytest_bdd import scenario, given, when, then
from requests.models import Response
import requests
from json import loads
import os
import tests.requestBodies.buildProductRequestBody as buildProductRequestBody
import tests.responseBodies.buildJSONEndpointResponseBody as buildJSONEndpointResponseBody
import tests.constants as constants
from jsonpath_rw import jsonpath, parse

@scenario('../features/jsonEndpoint.feature', 'Check Status Code')
def test_status_code():
    print("\nTest status code")

@pytest.fixture
def json_shared_data():
    baseUrl = constants.URL + "/" + constants.JSONENDPOINT
    request = ""
    response = Response()
    response_time = time.time()

    return [baseUrl, request, response, response_time]

@given("I have the endpoint - json")
def given_i_have_the_endpoint(json_shared_data):
    baseUrl, request, response, response_time = json_shared_data    

@when("I make the <requestType> request")
def when_i_make_the_request(requestType, json_shared_data):
    baseUrl, request, response, response_time = json_shared_data   
    request = requestType
    if (requestType == "post"):
        requestBody = buildProductRequestBody.buildRequest("SAVINGS", "SAVINGS", 1.1)
        json_shared_data[2] = requests.post(baseUrl, data=requestBody)        
    else:
        json_shared_data[2] = requests.request(requestType, baseUrl)

@then("the request should return <status> status")
def then_the_request_should_return_status(status, json_shared_data):
    baseUrl, request, response, response_time = json_shared_data   
    assert response.status_code == int(status), 'For {} request, Expected {} but {} was returned'.format(request.upper(), status, response.status_code)

@scenario('../features/jsonEndpoint.feature', 'Check post json response body')
def test__post_json_response_body(json_shared_data):
    baseUrl, request, response, response_time = json_shared_data   
    print("\nTest post json response body")

@given('the user sends a POST request to the json endpoint')
def given_get_version_request(json_shared_data):
    baseUrl, request, response, response_time = json_shared_data   
    start_time = time.time()
    requestBody = buildProductRequestBody.buildRequest("LOANS", "SAVINGS", 1.1)
    json_shared_data[2] = requests.post(baseUrl, data=requestBody)   
    response_time = time.time() - start_time

@when('the server receives the request')
def server_receives_request(json_shared_data):
    baseUrl, request, response, response_time = json_shared_data   
    pass

@then('it returns a response body <responseBody>')
def check_response_body(responseBody, json_shared_data):
    baseUrl, request, response, response_time = json_shared_data   
    jsonResponse = buildJSONEndpointResponseBody.buildResponse("LOANS", "SAVINGS", 1.1)
    actualResponseJson = response.json()
    assert actualResponseJson["format"] == jsonResponse["format"], f'Response json format is {actualResponseJson["format"]}, it should be  {jsonResponse["format"]}'
    assert actualResponseJson["data"] == jsonResponse["data"], f'Response json data is {actualResponseJson["data"]}, it should be  {jsonResponse["data"]}'
    assert actualResponseJson['additional']['overall']['result'] == "Accept" or "Decline", f'Response json additional overall result is neither Accept nor Decline'
    assert len(actualResponseJson['additional']['decisions']) >= 0, f'Response json additional decisions are 0'
    for decision in actualResponseJson['additional']['decisions']:
        for key in decision:
            assert decision[key]['result'] == "Accept" or "Decline", f'Response json additional decision result is neither Accept nor Decline'
            assert isinstance(decision[key]['duration'], float), f'Response json additional decision result is neither Accept nor Decline'
    
    
@scenario('../features/jsonEndpoint.feature', 'Check non-post json response body')
def test_non_post_response_body(json_shared_data):
    baseUrl, request, response, response_time = json_shared_data   
    print("\nTest non post response body")

@given('the user sends a <requestType> request to the version endpoint')
def given_non_get_version_request(requestType, json_shared_data):
    baseUrl, request, response, response_time = json_shared_data   
    requestBody = buildProductRequestBody.buildRequest("LOANS", "SAVINGS", 1.1)
    pytest.response = requests.request(requestType, baseUrl, data=requestBody)
    

@then('it returns a method not allowed response body <responseBody>')
def check_response_body(responseBody, json_shared_data):
    baseUrl, request, response, response_time = json_shared_data   
    with open(os.path.join('responseBodies', responseBody)) as f:
        expected_response = loads(f.read())
    assert pytest.response.json() == expected_response, f'Response was {response.json()}, it should be {expected_response}'

@then("The 'rule[Code]' section would be duplicated in the response per rule execution.")
def check_rule_code(json_shared_data):
    baseUrl, request, response, response_time = json_shared_data   
    response_body = response.json()
    for decision in response_body['additional']['decisions']:
        for key in decision:
            jsonpath_expr = parse(f'$.additional.decisions[*].{key}')
            matches = jsonpath_expr.find(response_body)
            assert len(matches) == 1, f'Expected multiple rule[Code] sections in the response, but found {len(matches)}'


@then("the response time should be less than 200ms")
def check_json_response_time(json_shared_data):
    baseUrl, request, response, response_time = json_shared_data   
    assert response_time < 0.2, f'Response time was {response_time} seconds, it should be less than 0.2 seconds'
