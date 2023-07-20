import requests

api_url = "https://example.com/api/user_data"
auth_token = "your_auth_token"

headers = {"Authorization": f"Bearer {auth_token}"}

response = requests.get(api_url, headers=headers)
user_data = response.json()
print(user_data)
