# Weather-Reporter
Program Purpose

The weather reporter is a command-line python application that retrieves live weather information for a city using the OpenWeatherMap API. The program asks the user to enter a city name, validates the input, retrieves current weather information and displays a weather report.

Files

reporter.py
This is the main python program it retrieves and validates a city name from the user.
It sends a GET request to the OpenWeatherMap API.
Analyzes the API response using JSON.
Displays the city, country, temperature, humidity, and weather description.
Saves the weather information to city_data.csv.
It reads the CSV file and reports the stored cities and temperatures.

city_data.csv
This file stores weather information retrieved from the OpenWeatherMap API.
The file stores:
City
Country
Temperature (C)
Humidity (%)
Description


