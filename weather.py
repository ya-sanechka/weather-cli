import os
import sys
import requests
from dotenv import load_dotenv


def main():
    load_dotenv()
    api_key = os.getenv("WEATHER_API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?q=Moscow&appid={api_key}&units=metric"
    response = requests.get(url).json()

    if response.get("cod") != 200:
        print(f"ошибка api: {response.get('message')}")
        sys.exit(1)

    print(f"Погода в Москве: {response['weather'][0]['description']}")
    print(f"Температура: {response['main']['temp']}°C")
    print(f"Влажность: {response['main']['humidity']}%")
    print(f"Давление: {response['main']['pressure']} гПа")
    print(f"Скорость ветра: {response['wind']['speed']} м/с")


if __name__ == "__main__":
    main()