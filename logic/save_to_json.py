import json
import os

import json
import os

def save_book_info(book_info, file_name):
    data = []
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as file:
            data = json.load(file)

        book_id = int(book_info['id'])

        if any(int(book['id']) == book_id for book in data):
            print(f"Libro con ID {book_id} ya existe. No se guardará.")
            return

        data.append(book_info)
        data.sort(key=lambda x: int(x['id']))

    else:
        data.append(book_info)

    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)



def get_last_saved_id(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as file:
            data = json.load(file)
            data.sort(key=lambda x: x['id'])  

            if data:
                return int(data[-1]['id'])
    return 99  
