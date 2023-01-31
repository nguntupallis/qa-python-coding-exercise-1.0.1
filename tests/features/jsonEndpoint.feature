@json
Feature: jsonEndpoint

Scenario: Check Status Code
    Given I have the endpoint - json
    When I make the <requestType> request
    Then the request should return <status> status
    
    Examples:
    | requestType  | status    |
    | get          | 405       |
    | post         | 200       |
    | put          | 405       |
    | patch        | 405       |
    | delete       | 405       |

Scenario: Check post json response body
    Given the user sends a POST request to the json endpoint
    When the server receives the request
    Then it returns a response body <responseBody>
    And The 'rule[Code]' section would be duplicated in the response per rule execution.

    Examples:
    | responseBody        |
    | jsonResponse.json   |


Scenario: Check non-post json response body
    Given the user sends a <requestType> request to the version endpoint
    When the server receives the request
    Then it returns a method not allowed response body <responseBody>

    Examples:
    | requestType   | responseBody                    |
    | get           | methodNotAllowedResponse.json   |
    | put           | methodNotAllowedResponse.json   |
    | patch         | methodNotAllowedResponse.json   |
    | delete        | methodNotAllowedResponse.json   |


Scenario: /json endpoint responds within 200ms
    Given the user sends a POST request to the json endpoint
    When the server receives the request
    Then the response time should be less than 200ms