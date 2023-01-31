@xml
Feature: xmlEndpoint

Scenario: Check Status Code
Given I have the endpoint - xml
When I make the <requestType> request
Then the request should return <status> status

Examples:
| requestType  | status    |
| get          | 200       |
| post         | 201       |
| put          | 405       |
| patch        | 405       |
| delete       | 405       |

Scenario: Check query parameter
Given the query parameter <queryParameter> is set to <value>
When a user makes a GET request to the /xml endpoint
Then the response should <expectedResponse> additional debug information in the XML format

Examples:
| queryParameter  | value    | expectedResponse |
| debug           | true     | include          |
| debug           | false    | not include      |
|                 |          | not include      |

Scenario: Provide invalid parameter
Given the query parameter <queryParameter> is set to <value>
When a user makes a GET request to the /xml endpoint
Then the response should be <expectedResponse>

Examples:
| queryParameter  | value    | expectedResponse       |
| debug           | invalid  | invalidXMLRequest.json |

Scenario: Overall outcome is "Accept" unless one of the rules has an outcome of "Decline"
Given I have the endpoint - xml
When a user makes a GET request to the /xml endpoint
Then the overall outcome should be "Accept" unless one of the rules has an outcome of "Decline" in which case the overall result should be "Decline"

