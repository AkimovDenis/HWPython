# Многопоточное, асинхронное и мультипроцессорное программирование.
# Выполните следующее задание: 
# Задание №1 

# а) Напишите функцию, которая будет создавать файл, с задержкой 1 секунду. 
import os
import time
from threading import Thread

def create_file(filename):
    time.sleep(1)
    with open(filename, "w") as file:
        file.write(f"Это файл: {filename}")
    print(f"Файл {filename} создан.")

# б) Запустите циклом 100 таких функций, а также замерьте время. 
def sequential_execution():
    start_time = time.time()
    for i in range(100):
        create_file(f"file_{i + 1}.txt")
    end_time = time.time()
    print(f"Последовательное выполнение заняло {end_time - start_time:.2f} секунд.")

# в) Добавьте функционал многопоточного запуска, с замером времени. 
def multithreaded_execution():
    start_time = time.time()
    threads = []
    for i in range(100):
        thread = Thread(target = create_file, args = (f"file_{i + 1}.txt",))
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
