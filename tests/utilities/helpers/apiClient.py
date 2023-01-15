import json
import requests
from requests.models import Response

class apiClient:
    Response()

    def _init_(self, get_Request):
            self.get_Request = get_Request()

def get_Request(url: str, headers: any):
    if headers is None:
        response = requests.get(url)
    else:
        response = requests.get(url, headers=headers)
    return response

def post_Request(url: str, body: any):
    if body is None:
        response = requests.post(url)
    else:
        response = requests.post(url, json.stringify(body))