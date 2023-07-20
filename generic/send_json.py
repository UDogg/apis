import requests

api_url = "https://example.com/api/get_json_data"

response = requests.get(api_url)
json_data = response.json()
print(json_data)
