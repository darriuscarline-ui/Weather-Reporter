import csv
import json
import requests


API_KEY = "PUTYOURAPIKEYHERE"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_city():
    """Ask the user for a city and validate the input."""
    while True:
        city = input("Enter a city name: ").strip()

        if city:
            return city

        print("City name cannot be empty. Please try again.")


def get_weather(city):
    """Get weather information for a city from OpenWeatherMap."""
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)

        if response.status_code == 404:
            print("City not found. Please check the city name.")
            return None

        if response.status_code == 401:
            print("Invalid API key.")
            return None

        response.raise_for_status()

        weather_data = json.loads(response.text)

        return {
            "City": weather_data["name"],
            "Country": weather_data["sys"]["country"],
            "Temperature (C)": weather_data["main"]["temp"],
            "Humidity (%)": weather_data["main"]["humidity"],
            "Description": weather_data["weather"][0]["description"]
        }

    except requests.exceptions.RequestException as error:
        print(f"Error connecting to the weather API: {error}")
        return None


def save_weather(weather):
    """Save weather information to the CSV file."""
    file_name = "city_data.csv"

    try:
        with open(file_name, "a", newline="", encoding="utf-8") as file:
            fieldnames = [
                "City",
                "Country",
                "Temperature (C)",
                "Humidity (%)",
                "Description"
            ]

            writer = csv.DictWriter(file, fieldnames=fieldnames)

            if file.tell() == 0:
                writer.writeheader()

            writer.writerow(weather)

        print("Weather information saved to city_data.csv.")

    except OSError as error:
        print(f"Error writing to the CSV file: {error}")


def read_weather():
    """Read the CSV file and report the stored cities."""
    file_name = "city_data.csv"

    try:
        with open(file_name, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            cities = list(reader)

        print(f"\nNumber of cities in the file: {len(cities)}")

        if cities:
            print("Cities and temperatures:")

            for city in cities:
                print(
                    f"{city['City']}: "
                    f"{city['Temperature (C)']}°C"
                )
        else:
            print("No cities have been saved yet.")

    except FileNotFoundError:
        print("The city_data.csv file does not exist yet.")


def main():
    """Run the weather reporting program."""
    city = get_city()
    weather = get_weather(city)

    if weather:
        print("\nWeather Report")
        print("--------------------")
        print(f"City: {weather['City']}")
        print(f"Country: {weather['Country']}")
        print(f"Temperature: {weather['Temperature (C)']}°C")
        print(f"Humidity: {weather['Humidity (%)']}%")
        print(f"Description: {weather['Description']}")

        save_weather(weather)
        read_weather()


if __name__ == "__main__":
    main()