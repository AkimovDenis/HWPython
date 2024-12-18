import tkinter as tk
from tkinter import messagebox, filedialog
import requests
import json
import os

class JSONPlaceholderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Запрос данных с JSONPlaceholder")
        self.root.geometry("600x530")
        self.root.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Введите ID:", font=("Arial", 12)).pack(pady=10)
        self.id_entry = tk.Entry(self.root, width=30, font=("Arial", 12))
        self.id_entry.pack(pady=5)

        tk.Button(self.root, text="Получить данные", command=self.fetch_data, font=("Arial", 12), bg="lightblue").pack(pady=10)
        tk.Button(self.root, text="Сохранить объект", command=self.save_data, font=("Arial", 12), bg="lightblue").pack(pady=10)
        tk.Button(self.root, text="Закрыть", command=self.exit_program, font=("Arial", 12), bg="lightblue").pack(pady=10)

        self.result_text = tk.Text(self.root, width=70, height=15, font=("Courier", 10))
        self.result_text.pack(pady=10)

    def fetch_data(self):
        post_id = self.id_entry.get()

        if not post_id.isdigit():
            messagebox.showerror("Ошибка", "ID должен быть числом.")
            return

        url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                self.display_result(data)
            else:
                messagebox.showinfo("Ошибка", f"Данные с ID {post_id} не найдены.")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось выполнить запрос: {e}")

    def display_result(self, data):
        self.result_text.delete("1.0", tk.END)
        formatted_data = json.dumps(data, indent=4, ensure_ascii=False)
        self.result_text.insert(tk.END, formatted_data)

    def save_data(self):
        data = self.result_text.get("1.0", tk.END).strip()
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

    def exit_program(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = JSONPlaceholderApp(root)
    root.mainloop()