import requests

api_url = "https://example.com/api/get_image"

response = requests.get(api_url)
with open("image.jpg", "wb") as f:
    f.write(response.content)
