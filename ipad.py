import requests

api_url ="https://api.ipify.org?format=json"

response = requests.get(api_url)

print(f"Response status code is:{response.status_code}")

response_json = response.json()

print(response_json)