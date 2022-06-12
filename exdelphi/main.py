import requests
import json


BASE_URL = "http://api.exdelphi.com"
HEADERS = {'Content-Type': 'application/json',
           'Authorization': ''}

def run():
    pass

def authorize(username: str, password: str) -> None:
    """Sets headers to contain authorization token generated from given username and password"""
    response = requests.post(url=f"{BASE_URL}/token", data={"username": username, "password": password})
    response_content = json.loads(response.text)
    token = response_content['access_token']
    HEADERS['Authorization'] = f'Bearer {token}'
    print(f"Authenticated {username} at {BASE_URL}")

