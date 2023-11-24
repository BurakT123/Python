import requests


api_key = "dc17bef1817a2b7442faa1918d83373e"

api_url = "https://api.openweathermap.org/data/2.5/weather"

city = input("Write a city: ")
response = requests.get(
    url = api_url,
    params={
        "q" : city,
        "appid" : api_key,
        "units" : "metric"
    }
)

weather_data = response.json()
print(city,"temperature is :",weather_data['main']['temp'])