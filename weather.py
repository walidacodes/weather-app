import requests

API_KEY = "fdffac31a60f17fe3c9b78f38ef6876d"  # Replace with your OpenWeatherMap API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()

def main():
    city = input("Enter city name: ")
    weather_data = get_weather(city)

    if weather_data.get("cod") != 200:
        print("City not found!")
    else:
        city_name = weather_data["name"]
        temperature = weather_data["main"]["temp"]
        weather_description = weather_data["weather"][0]["description"]
        print(f"\nWeather in {city_name}:")
        print(f"Temperature: {temperature}°C")
        print(f"Condition: {weather_description}")

if __name__ == "__main__":
    main()
