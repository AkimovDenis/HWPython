# Задание №1 
# а) Загрузите массив json – объектов с сайта jsonplaceholder, используя библиотеку requests. 

import requests
import aiohttp
import asyncio
import os
import json

FOLDER_NAME = "json_files"
os.makedirs(FOLDER_NAME, exist_ok = True)
URL = "https://jsonplaceholder.typicode.com/photos"

def fetch_json_with_requests():
    print("Загрузка с помощью requests...")
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        print(f"Успешно загружено {len(data)} объектов.")
        return data
    else:
        print(f"Ошибка загрузки: {response.status_code}")
        return []
    
# б) Сохраните циклом каждый в отдельный файл, в одну новую папку. 
def save_to_file(data, folder, filename):
    with open(os.path.join(folder, filename), "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent = 4)
    print(f"Файл сохранён: {filename}")

def save_json_with_requests():
    data = fetch_json_with_requests()
    for index, item in enumerate(data, start=1):
        save_to_file(item, FOLDER_NAME, f"item_{index}_requests.json")

print("\nСохранение JSON-объектов с requests:")
save_json_with_requests()

# а) Загрузите массив json – объектов с сайта jsonplaceholder, используя библиотеку aiohttp. 
async def fetch_json_with_aiohttp():
    print("Загрузка с помощью aiohttp...")
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as response:
            if response.status == 200:
                data = await response.json()
                print(f"Успешно загружено {len(data)} объектов.")
                return data
            else:
                print(f"Ошибка загрузки: {response.status}")
                return []

# б) Сохраните циклом каждый в отдельный файл, в одну новую папку.
async def save_json_with_aiohttp():
    data = await fetch_json_with_aiohttp()
    for index, item in enumerate(data, start = 1):
        save_to_file(item, FOLDER_NAME, f"item_{index}_aiohttp.json")

print("\nСохранение JSON-объектов с aiohttp:")
asyncio.run(save_json_with_aiohttp())