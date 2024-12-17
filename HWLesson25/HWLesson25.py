# Задание №1 
# б) Разработать программу на библиотеке tkinter. 

import tkinter as tk
from tkinter import messagebox, filedialog
import requests
import json
import os

def fetch_data():
    post_id = id_entry.get()

    if not post_id.isdigit():
        messagebox.showerror("Ошибка", "ID должен быть числом.")
        return

    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            result_text.delete("1.0", tk.END)
            result_text.insert(tk.END, json.dumps(data, indent=4))
        else:
            messagebox.showinfo("Ошибка", f"Данные с ID {post_id} не найдены.")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось выполнить запрос: {e}")

# в) Реализовать сохранение полученного объекта в папку.
def save_data():
    data = result_text.get("1.0", tk.END).strip()
    if not data:
        messagebox.showinfo("Ошибка", "Нет данных для сохранения.")
        return

    save_path = filedialog.askdirectory(title="Выберите папку для сохранения файла")
    if save_path:
        file_name = os.path.join(save_path, "json_data.json")
        try:
            with open(file_name, "w", encoding="utf-8") as file:
                file.write(data)
            messagebox.showinfo("Успех", f"Данные сохранены в {file_name}.")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось сохранить файл: {e}")

def exit_program():
    window.destroy()

def MessageBox1():
    messagebox.showinfo("Информация", f"Кнопка работает")

window = tk.Tk()
window.title("Запрос данных с JSONPlaceholder")
window.geometry("600x530")
window.resizable(False, False)

tk.Label(window, text="Введите ID:", font=("Arial", 12)).pack(pady=10)

id_entry = tk.Entry(window, width=30, font=("Arial", 12))
id_entry.pack(pady=5)

tk.Button(window, text="Получить данные", command=fetch_data, font=("Arial", 12), bg="lightblue").pack(pady=10)

result_text = tk.Text(window, width=70, height=15, font=("Courier", 10))
result_text.pack(pady=10)

tk.Button(window, text="Сохранить объект", command=save_data, font=("Arial", 12), bg="lightblue").pack(pady=10)

tk.Button(window, text="Закрыть", command=exit_program, font=("Arial", 12), bg="lightblue").pack(pady=10)

window.mainloop()
