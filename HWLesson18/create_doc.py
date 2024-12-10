# б) Напишите пример приложения на input, которое получает текст от 
# пользователя и создаёт word-файл с этим текстом

import time
from docx import Document 

def create_word_file():
    user_text = input("Введите текст для Word-документа: ")
    doc = Document()
    doc.add_paragraph(user_text)

    file_name = "user_text.docx"
    doc.save(file_name)
    print(f"Документ сохранен как '{file_name}'")
    time.sleep(2)

create_word_file()