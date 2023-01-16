import json

class buildJSONEndpointResponseBody:
    json
    
def buildResponse(productName, productType, productVersion):
    postJSONresponse = {
            "format": "JSON",
            "data": {
                "product_name": productName,
                "product_type": productType,
                "product_version": productVersion
            },
            "additional": {
                "overall": {
                    "duration": 0.7389,
                    "result": "Decline"
                },
                "decisions": [
                    {
                        "ruleA0": {
                            "duration": 0.5697355390322274,
                            "result": "Accept"
                        }
                    },
                    {
                        "ruleA1": {
                            "duration": 0.4066016138377657,
                            "result": "Accept"
                        }
                    },
                    {
                        "ruleA2": {
                            "duration": 0.7443247001666076,
                            "result": "Accept"
                        }
                    },
                    {
                        "ruleA3": {
                            "duration": 0.4997689545470194,
                            "result": "Decline"
                        }
                    },
                    {
                        "ruleA4": {
                            "duration": 0.6299761904302644,
                            "result": "Accept"
                        }
                    },
                    {
                        "ruleA5": {
                            "duration": 0.34282336759986487,
                            "result": "Accept"
                        }
                    },
                    {
                        "ruleA6": {
                            "duration": 0.2659694102105954,
                            "result": "Accept"
                    }
                }
            ]
        }
    }
    return postJSONresponse
    

