import pytest
from pytest_bdd import scenario, given, when, then
from requests.models import Response
import requests
from json import loads
import os
from bs4 import BeautifulSoup
import tests.constants as constants
from tests.utilities.helpers.apiClient import apiClient

@scenario('../features/xmlEndpoint.feature', 'Check Status Code')
def test_status_code():
    print("\nTest status code")

@pytest.fixture
def xml_shared_data():
    baseUrl = constants.URL + "/" + constants.XMLENDPOINT
    request = ""
    response = Response()

    return [baseUrl, request, response]

@given("I have the endpoint - xml")
def given_i_have_the_endpoint(xml_shared_data):
    baseUrl, request, response = xml_shared_data    


@when("I make the <requestType> request")
def when_i_make_the_request(requestType, xml_shared_data):
    baseUrl, request, response = xml_shared_data   
    request = requestType
    xml_shared_data[2] = requests.request(requestType, baseUrl)

@then("the request should return <status> status")
def then_the_request_should_return_status(status, xml_shared_data):
    baseUrl, request, response = xml_shared_data    
    assert response.status_code == int(status), 'For {} request, Expected {} but {} was returned'.format(request.upper(), status, response.status_code)

@scenario('../features/xmlEndpoint.feature', 'Check query parameter')
def test_query_parameter(xml_shared_data):
    baseUrl, request, response = xml_shared_data    
    print("\nCheck query parameter")

@given("the query parameter <queryParameter> is set to <value>")
def set_query_parameter(queryParameter, value, xml_shared_data):
    baseUrl, request, response = xml_shared_data    
    if (queryParameter != "" or value != ""):
        xml_shared_data[0]= constants.URL + "/" + constants.XMLENDPOINT + "?" + queryParameter + "=" + value
    else:
        xml_shared_data[0] = constants.URL + "/" + constants.XMLENDPOINT

@when("a user makes a GET request to the /xml endpoint")
def get_xml_endpoint(xml_shared_data):
    baseUrl, request, response = xml_shared_data    
    xml_shared_data[2] = requests.get(baseUrl)

@then("the response should <expectedResponse> additional debug information in the XML format")
def check_response(expectedResponse, xml_shared_data):
    baseUrl, request, response = xml_shared_data    
    soup = BeautifulSoup(response.content, 'lxml')
    debug = soup.find('debug')
    if expectedResponse == "include":
        assert debug is not None, "Debug information not found in the response"
        print("Assertion passed: Debug information found in the response.")  
    else:
        assert debug is None, "Debug information is found in the response"
        print("Assertion passed: Debug information not found in the response.")  

@scenario('../features/xmlEndpoint.feature', 'Provide invalid parameter')
def test_invalid_parameter(xml_shared_data):
    baseUrl, request, response = xml_shared_data   
    print("\Provide invalid parameter")

@then("the response should be <expectedResponse>")
def test_response_value_invalid(expectedResponse, xml_shared_data):
    baseUrl, request, response = xml_shared_data   
    assert response.status_code == 400, 'Expected {} but {} was returned'.format(400, response.status_code)   
    with open(os.path.join('responseBodies', expectedResponse)) as f:
        expected_response = loads(f.read())
    assert response.json() == expected_response, 'Expected {} but {} was returned'.format(expected_response, response.json())   

@scenario('../features/xmlEndpoint.feature', 'Overall outcome is "Accept" unless one of the rules has an outcome of "Decline"')
def test_overall_outcome(xml_shared_data):
    baseUrl, request, response = xml_shared_data    
    print("\Overall outcome")

@then('the overall outcome should be "Accept" unless one of the rules has an outcome of "Decline" in which case the overall result should be "Decline"')
def overall_outcome_verification(xml_shared_data):
    baseUrl, request, response = xml_shared_data    
    soup = BeautifulSoup(response.content, 'lxml')
    overall_decision = soup.find('overall').text
    rule_decisions = [rule.text for rule in soup.find_all('rule')]
    assert all(d == 'Accept' for d in rule_decisions) and overall_decision == 'Accept', "Not all decisions are Accept"