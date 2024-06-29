import requests
import pandas as pd
import pprint

# url = 'https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=fnd&lang=en'
# data = requests.get(url)
# data_json = data.json()

# data_json_weather = data_json['weatherForecast']
# print("Welcome to my weather forecast")
# date = input('Please enter the date you want to get the weather forecast? (YYYYMMDD) ')

# for i in range(0,len(data_json_weather)):
#     json = data_json_weather[i]
#     if json['forecastDate'] == date:
#         json_chosen = json

# print("What can I help you today?")
# while True:
#     print(f"1. Weather description of {date}")
#     print(f"2. Wind description of {date}")
#     print(f"3. Maximum and minimum temperature of {date}\n")
#     print("Or You can press q to quit")
    
#     choice = input("What would you like to do? ").lower()
#     if choice == "q":
#         break
#     elif choice == "1":
#         print(json_chosen['forecastWeather'])
#     elif choice == "2":
#         print(json_chosen['forecastWind'])
#     elif choice == "3":
#         print(f"Maximum temperature of {date}: ", json_chosen['forecastMaxtemp']['value'], "°C", sep= "")
#         print(f"Minimum temperature of {date}: ", json_chosen['forecastMintemp']['value'], "°C",sep= "")

    
    
# print("Thanks for using my weather forecast service")


def get_json(url):
    data = requests.get(url)
    data_json = data.json()
    data_json_weather = data_json['weatherForecast']
    return data_json_weather

def get_chosen_json(date, whole_json) -> dict:
    # date = input('Please enter the date you want to get the weather forecast? (YYYYMMDD) ')
    for i in range(0,len(whole_json)):
        json = whole_json[i]
        if json['forecastDate'] == date:
            json_chosen = json
    return json_chosen

def get_weather_summary(single_json) -> str:
    weather_summary = single_json['forecastWeather']
    return weather_summary

def get_wind_summary(single_json) -> str:
    wind_summary = single_json['forecastWind']
    return wind_summary

def get_temperature_summary(single_json) -> str:
    max_temp = single_json['forecastMaxtemp']['value']
    min_temp = single_json['forecastMintemp']['value']
    return f"Maximum temperature: {max_temp}°C, Minimum temperature: {min_temp}°C"

def main():
    url = 'https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=fnd&lang=en'
    whole_json = get_json(url)
    print('welcome to my weather forecast!')

    date = input('Please enter the date you want to get the weather forecast? (YYYYMMDD) ')
    single_json = get_chosen_json(date, whole_json)

    print(f"1. Weather description of {date}")
    print(f"2. Wind description of {date}")
    print(f"3. Maximum and minimum temperature of {date}\n")
    
    while True:
        command = input("Enter a command (q to quit): ").lower()
        if command == 'q':
            break
        elif command == '1':
            print('Weather Summary:')
            print(get_weather_summary(single_json), "\n")
        elif command == '2':
            print('Wind Summary:')
            print(get_wind_summary(single_json), "\n")
        elif command == '3':
            print('Temperature Summary:')
            print(get_temperature_summary(single_json), "\n")
        else:
            print('Invalid command. Please try again')
            print(f"1. Weather description of {date}")
            print(f"2. Wind description of {date}")
            print(f"3. Maximum and minimum temperature of {date}\n")

    print("Thanks for using my weather forecast service")

if __name__ == '__main__':
    main()