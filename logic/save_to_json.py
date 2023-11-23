# logic/save_to_json.py

import json
import os

def save_book_info(book_info, file_name):
    data = []
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as file:
            data = json.load(file)
    
    data.append(book_info)

    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def get_last_saved_id(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            data = json.load(file)
            if data:
                return int(data[-1]['id'])  # Asumiendo que 'id' está siempre presente y es un entero
    return 99  # Retorna 99 si el archivo no existe o está vacío, para comenzar en 100
