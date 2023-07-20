import requests

api_key = "your_weather_api_key"
city_name = "New York"

api_url = f"https://example.com/api/weather"
params = {"q": city_name, "appid": api_key}

response = requests.get(api_url, params=params)
weather_data = response.json()
print(weather_data)
