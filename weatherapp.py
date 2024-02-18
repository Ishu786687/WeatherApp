import requests
from datetime import datetime

user_api = "7148b85349024ceeac5338c226407089"
location = input("enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api

api_link = requests.get(complete_api_link)
api_data = api_link.json()
# print(api_data)
if api_data['cod'] == '404':
    print(f"Invalid city: {location},Please check your city name")
else:
    temp_city = ((api_data['main']['temp'])-273.15)
    weather_desc = api_data['weather'][0]['description']
    hmd = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S: %p")
    
    print("------------------------------------------------------------------")
    print(f"Weather Stats for {location.upper()} || {date_time}")
    print("------------------------------------------------------------------")
    print(f"Current Temperature is : {temp_city}deg C")
    print(f"Current weather desc : {weather_desc}")
    print(f"Current Humidity : {hmd} %")
    print(f"Current wind speed : {wind_spd} kmph")