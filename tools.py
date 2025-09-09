import re

# Tools
def add(a: int, b: int) -> int:
    return a + b

def multiply(a: int, b: int) -> int:
    return a * b

def subtract(a: int, b: int) -> int:
    return a - b

def divide(a: int, b: int):
    if b == 0:
        return "Error: Division by zero!"
    return a / b

def get_weather(city: str) -> str:
    weather_data = {
        "Karachi": "34°C",
        "Lahore": "36°C",
        "Islamabad": "32°C",
        "London": "20°C",
        "New York": "25°C"
    }
    return weather_data.get(city, "City not found")


# Agent function
def agent(user_input: str):
    # ✅ Math checks
    match_add = re.search(r"(\d+)\s*\+\s*(\d+)", user_input)
    if match_add:
        a, b = int(match_add.group(1)), int(match_add.group(2))
        return f"The answer is {add(a, b)} ✅"
    
    match_mul = re.search(r"(\d+)\s*\*\s*(\d+)", user_input)
    if match_mul:
        a, b = int(match_mul.group(1)), int(match_mul.group(2))
        return f"The answer is {multiply(a, b)} ✅"
    
    match_sub = re.search(r"(\d+)\s*-\s*(\d+)", user_input)
    if match_sub:
        a, b = int(match_sub.group(1)), int(match_sub.group(2))
        return f"The answer is {subtract(a, b)} ✅"
    
    match_div = re.search(r"(\d+)\s*/\s*(\d+)", user_input)
    if match_div:
        a, b = int(match_div.group(1)), int(match_div.group(2))
        return f"The answer is {divide(a, b)} ✅"

    #Weather check
    match_weather = re.search(r"weather in ([a-zA-Z ]+)", user_input, re.IGNORECASE)
    if match_weather:
        city = match_weather.group(1).strip()
        return f"The weather in {city} is {get_weather(city)} 🌤️"

    return "Sorry, I can only solve math (+, -, *, /) and weather questions."


print(agent("5+5"))
print(agent("10-3"))
print(agent("6*7"))
print(agent("20/4"))
print(agent("weather in Karachi"))
print(agent("weather in London"))
print(agent("Tell me weather in New York"))
print(agent("what is the population of karachi?"))