@version
Feature: versionEndpoint

    Scenario: Check Status Code
    Given I have the endpoint - version
    When I make the <requestType> request
    Then the request should return <status> status

    Examples:

    | requestType  | status    |
    | get          | 200       |
    | post         | 405       |
    | put          | 405       |
    | patch        | 405       |
    | delete       | 405       |