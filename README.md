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

Libraries Used
This project uses requests which is used to send a GET request to the OpenWeatherMap API.
json which is used to analyze the JSON data returned by the API.
csv which is used to write weather information to and read information from the CSV file.

How to get a OpenWeatherMap API
1. Go to OpenWeatherMap
2. Create a free account or sign into an exisiting account.
3. Go to your account's API Keys section
4. Create or copy and API key.
5. Open reporter.py in VS Code
6. Find the following line: API_KEY = "PUTYOURAPIKEYHERE"
7. Replace "PUTYOURAPIKEYHERE" with your own OpenWeatherMap API key. (It might take a little while until your key works so don't panic if it doesn't work immediately after creating)

Installation
Python 3 and the requests library are required
Install the requests library from the termina: pip install request

How to Run
1. Put both reporter.py and city_data.csv into Weather Reporter folder.
2. Open Weather Reporter folder in VS Code.
3. Make sure your OpenWeatherMap API keyhas been added to reporter.py.
4. Open the terminal.
5. Run the program: reporter.py
6. Enter a city name when prompted.
The program will display the current weather information and save the results to city_data.csv

Example Output
Enter a city name: San Diego

Weather Report
--------------------
City: San Diego
Country: US
Temperature: 30.89°C
Humidity: 38%
Description: clear sky

Weather information saved to city_data.csv.

Number of cities in the file: 3
Cities and temperatures:
Minneapolis: 14.25°C
Chicago: 18.88°C
San Diego: 30.89°C

The temperature and weather will change because the program retrieves live data from the API.
