import requests

api_url = "https://example.com/api/geolocation"
latitude = 37.7749
longitude = -122.4194

response = requests.get(api_url, params={"lat": latitude, "lon": longitude})
geolocation_data = response.json()
print(geolocation_data)
