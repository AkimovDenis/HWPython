# Задание №1 
# а) Загрузите циклом 10 рандомных картинок с сайта используя библиотеку 
# requests, затем aiohttp. 
# б) Сохраните их в разные папки циклом.

import os
import requests
import aiohttp
import asyncio
import random

BASE_URL = "https://picsum.photos/200/300"

folderRequests = "images_requests"
folderAiohttp = "images_aiohttp"

os.makedirs(folderRequests, exist_ok = True)
os.makedirs(folderAiohttp, exist_ok = True)

def download_images_with_requests():
    print("Загрузка изображений с помощью requests...")
    for i in range(1, 11):
        response = requests.get(BASE_URL)
        if response.status_code == 200:
            filename = os.path.join(folderRequests, f"image_{i}.jpg")
            with open(filename, "wb") as file:
                file.write(response.content)
            print(f"Изображение {i} сохранено как {filename}")
        else:
            print(f"Ошибка загрузки изображения {i}: {response.status_code}")


async def download_images_with_aiohttp():
    print("Загрузка изображений с помощью aiohttp...")
    async with aiohttp.ClientSession() as session:
        for i in range(1, 11):
            async with session.get(BASE_URL) as response:
                if response.status == 200:
                    filename = os.path.join(folderAiohttp, f"image_{i}.jpg")
                    with open(filename, "wb") as file:
                        file.write(await response.read())
                    print(f"Изображение {i} сохранено как {filename}")
                else:
                    print(f"Ошибка загрузки изображения {i}: {response.status}")

print("\nСохранение изображений с requests:")
download_images_with_requests()

print("\nСохранение изображений с aiohttp:")
asyncio.run(download_images_with_aiohttp())

# а) Получить погоду в Астане с статического сайта погоды, используя 
# string.split() 
print("\n====== Информация о погоде в Астане на данный момент, полученная используя string.split() ======")

def fetch_weather_with_split():
    url = "https://www.gismeteo.ru/weather-astana-5164/now/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers = headers, timeout = 10)
        response.raise_for_status()

        html_content = response.text[:20000]
        print("HTML успешно загружен!")

        if '"weather":{"cw":' in html_content:
            weather_data = html_content.split('"weather":{"cw":')[1].split("}}")[0]

            description = extract_field_value(weather_data, '"description":')

            humidity = extract_field_value(weather_data, '"humidity":')

            pressure = extract_field_value(weather_data, '"pressure":')

            temperature_air = extract_field_value(weather_data, '"temperatureAir":')

            temperature_heat_index = extract_field_value(weather_data, '"temperatureHeatIndex":')

            wind_speed = extract_field_value(weather_data, '"windSpeed":')
            print(f"Общее описание погоды: {description}")
            print(f"Влажность: {humidity}%")
            print(f"Давление: {pressure} мм рт. ст.")
            print(f"Температура воздуха: {temperature_air}°C")
            print(f"Температура по ощущениям: {temperature_heat_index}°C")
            print(f"Скорость ветра: {wind_speed} м/с")
        else:
            print("Раздел 'weather' не найден в HTML-коде.")

    except requests.exceptions.RequestException as e:
        print(f"Ошибка запроса: {e}")

def extract_field_value(data, field):
    if field in data:
        return data.split(field)[1].split(",")[0].strip().strip('[]"')
    return "Не найдено"

fetch_weather_with_split()

# б) Получить погоду в Астане с статического сайта погоды, используя bs4
print("\n====== Информация о погоде в Астане на данный момент, полученная используя bs4 ======")
from bs4 import BeautifulSoup

def fetch_weather_with_bs4():
    url = "https://www.gismeteo.ru/weather-astana-5164/now/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        print("HTML успешно загружен!")

        soup = BeautifulSoup(response.text, 'html.parser')

        weather_data = soup.find('script', string=lambda s: s and '"weather":{"cw":' in s)
        if weather_data:
            weather_json = weather_data.string.split('"weather":{"cw":')[1].split("}}")[0]

            description = extract_field_value(weather_json, '"description":')
            humidity = extract_field_value(weather_json, '"humidity":')
            pressure = extract_field_value(weather_json, '"pressure":')
            temperature_air = extract_field_value(weather_json, '"temperatureAir":')
            temperature_heat_index = extract_field_value(weather_json, '"temperatureHeatIndex":')
            wind_speed = extract_field_value(weather_json, '"windSpeed":')

            print(f"Общее описание погоды: {description}")
            print(f"Влажность: {humidity}%")
            print(f"Давление: {pressure} мм рт. ст.")
            print(f"Температура воздуха: {temperature_air}°C")
            print(f"Температура по ощущениям: {temperature_heat_index}°C")
            print(f"Скорость ветра: {wind_speed} м/с")
        else:
            print("Раздел с погодой не найден.")

    except requests.exceptions.RequestException as e:
        print(f"Ошибка запроса: {e}")

def extract_field_value(data, field):
    if field in data:
        return data.split(field)[1].split(",")[0].strip().strip('[]"')
    return "Не найдено"

fetch_weather_with_bs4()