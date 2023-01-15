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