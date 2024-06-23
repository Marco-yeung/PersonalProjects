import requests
import pandas as pd
import pprint

url = 'https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=fnd&lang=en'
data = requests.get(url)
data_json = data.json()

data_json_weather = data_json['weatherForecast']
print("Welcome to my weather forecast")
date = input('Please enter the date you want to get the weather forecast? (YYYYMMDD) ')

for i in range(0,len(data_json_weather)):
    json = data_json_weather[i]
    if json['forecastDate'] == date:
        json_chosen = json


while True:
    print("What can I help you today?")
    print(f"1. Weather description of {date}")
    print(f"2. Wind description of {date}")
    print(f"3. Maximum and minimum temperature of {date}\n")
    print("Or You can press q to quit")
    
    choice = input("What would you like to do? ").lower()
    if choice == "q":
        break
    elif choice == "1":
        print(json_chosen['forecastWeather'])
    elif choice == "2":
        print(json_chosen['forecastWind'])
    elif choice == "3":
        print(f"Maximum temperature of {date}: ", json_chosen['forecastMaxtemp']['value'], "°C", sep= "")
        print(f"Minimum temperature of {date}: ", json_chosen['forecastMintemp']['value'], "°C",sep= "")

    
    
print("Thanks for using my weather forecast service")