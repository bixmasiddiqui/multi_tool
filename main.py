import requests
import os

#for weather_agent
def get_weather(city: str) -> str:
    API_KEY = os.getenv("WEATHER_API_KEY") 
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        temp_c = data['current']['temp_c']
        condition = data['current']['condition']['text']
        return f"{city} me {temp_c}°C hai aur weather {condition} hai."
    else:
        return "Weather data fetch nahi hua."