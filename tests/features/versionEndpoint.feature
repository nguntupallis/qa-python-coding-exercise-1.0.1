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

Scenario: Check get version response body
Given the user sends a GET request to the version endpoint
When the server receives the request
Then it returns a response body <responseBody>

Examples:
| responseBody           |
| versionResponse.json   |

Scenario: Check non-get version response body
Given the user sends a <requestType> request to the version endpoint
When the server receives the request
Then it returns a response body <responseBody>

Examples:
| requestType   | responseBody                    |
| post          | methodNotAllowedResponse.json   |
| put           | methodNotAllowedResponse.json   |
| patch         | methodNotAllowedResponse.json   |
| delete        | methodNotAllowedResponse.json   |

