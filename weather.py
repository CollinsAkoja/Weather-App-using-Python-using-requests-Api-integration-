import requests

API_KEY = "6a7d6e677874cf9920c803244b355973"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if response.status_code == 200:
            city_name = data["name"]
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            description = data["weather"][0]["description"]
            wind = data["wind"]["speed"]

            print("\nWeather Report")
            print("----------------------")
            print(f"City: {city_name}")
            print(f"Temperature: {temp}°C")
            print(f"Humidity: {humidity}%")
            print(f"Weather: {description}")
            print(f"Wind Speed: {wind} m/s")

        else:
            print("City not found.")

    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)


if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)