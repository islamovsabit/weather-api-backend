import requests
API_KEY = 'ef63fe2670db1d5f8a38e84ba8132e69'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'


def get_weather(city):
    try:
        params = {
            'q': city,
            'appid': API_KEY,
            'units': 'metric'  # Use 'imperial' for Fahrenheit
        }
        response = requests.get(BASE_URL, params=params)

        if response.status_code == 200:
            weather_data = response.json()
            temperature = weather_data['main']['temp']
            description = weather_data['weather'][0]['description']

            print(f"Weather in {city}:")
            print(f"Temperature: {temperature}°C")
            print(f"Description: {description}")
        else:
            print(f"Error: City not found")
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == '__main__':
    city_name = input("Enter a city name: ")
    get_weather(city_name)
