# Задание №1 
# а) Напишите функцию, которая будет загружать информацию сразу с 100 
# ссылок. 

import requests
import aiohttp
import asyncio
import time

BASE_URL = "https://jsonplaceholder.typicode.com/photos/"
urls = [f"{BASE_URL}{i}" for i in range(1, 50)]

def fetch_all_urls_sequential(urls):
    start_time = time.time()
    responses = []
    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            responses.append(response.json())
    end_time = time.time()
    print(f"Последовательная загрузка заняла {end_time - start_time:.2f} секунд.")
    return responses

# б) Запустите эту функцию, а также замерьте время. 
print("Последовательная загрузка:")
fetch_all_urls_sequential(urls)

# в) Добавьте функционал асинхронного запуска, с замером времени.
async def fetch_url(session, url):
    async with session.get(url) as response:
        if response.status == 200:
            return await response.json()

async def fetch_all_urls_async(urls):
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        responses = await asyncio.gather(*tasks)
    end_time = time.time()
    print(f"Асинхронная загрузка заняла {end_time - start_time:.2f} секунд.")
    return responses

print("\nАсинхронная загрузка:")
asyncio.run(fetch_all_urls_async(urls))
