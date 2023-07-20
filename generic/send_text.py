import requests

api_url = "https://example.com/api/send_text"
text_data = "This is some text data to be sent."

response = requests.post(api_url, data=text_data)
print(response.status_code, response.json())
