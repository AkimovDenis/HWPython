# Задание №1 
# а) Напишите функцию, которая будет создавать файл и записывать в него 
# рандомное число, с задержкой 1 секунду. 

import os
import time
import random
from threading import Thread

def create_file_with_random_number(filename):
    time.sleep(1)
    random_number = random.randint(1, 1000)
    with open(filename, "w") as file:
        file.write(f"Случайное число: {random_number}")
    print(f"Файл {filename} создан с числом {random_number}.")

# б) Запустите циклом 1000 таких функций, а также замерьте время. 
def sequential_execution():
    start_time = time.time()
    for i in range(1000):
        create_file_with_random_number(f"file_{i + 1}.txt")
    end_time = time.time()
    print(f"Последовательное выполнение заняло {end_time - start_time:.2f} секунд.")

# в) Добавьте функционал мультипоточного запуска, с замером времени. 
# Обязательно посмотрите нагрузку на ЦП в этот момент (через диспетчер задач). 
def multithreaded_execution():
    start_time = time.time()
    threads = []
    for i in range(1000):
        thread = Thread(target = create_file_with_random_number, args=(f"file_{i + 1}.txt",))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f"Многопоточное выполнение заняло {end_time - start_time:.2f} секунд.")

if not os.path.exists("output_files"):
    os.makedirs("output_files")
os.chdir("output_files")

print("Запуск последовательного выполнения:")
sequential_execution()

print("\nЗапуск многопоточного выполнения:")
multithreaded_execution()
