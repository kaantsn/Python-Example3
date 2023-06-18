import requests
import json

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        if data["cod"] == 200:
            print(f"Hava Durumu: {data['weather'][0]['description']}")
            print(f"Sıcaklık: {data['main']['temp']} °C")
            print(f"Nem Oranı: {data['main']['humidity']}%")
        else:
            print("Hava durumu verileri alınamadı.")
    except requests.exceptions.RequestException as e:
        print("Hava durumu verileri alınırken bir hata oluştu:", e)

# API anahtarını ve şehir adını girin
api_key = "YOUR_API_KEY"
city = "Ankara"

get_weather(api_key, city)
