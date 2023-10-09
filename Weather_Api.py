import requests
import json

API_KEY = "d62bfda79aefd2aa3497b380bdfda076"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")

request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"

response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]["description"]
    print("Weather type of",city,"is :",weather)

    temperature = round(data["main"]["temp"]-273.15,2)
    print("Temperature of",city,"is :",temperature,"C")

else:
    print("An unknown error occured!")


