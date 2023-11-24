from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Thread
import sys
from logic.get_json_book import scrape_book_details
from logic.save_to_json import save_book_info, get_last_saved_id

stop_requested = False

def process_book(book_id):
    if stop_requested:
        return None  # Retorna None si se pide detener

    url = f'https://www.epublibre.org/libro/detalle/{book_id}'
    book_info = scrape_book_details(url)
    if book_info:
        save_book_info(book_info, 'books_data.json')
    return book_id

def input_thread():
    global stop_requested
    while True:
        user_input = input()
        if user_input.lower() == 's':
            stop_requested = True
            print("Deteniendo el proceso... Por favor, espere.")
            break

def main():
    global stop_requested

    start_id = get_last_saved_id('books_data.json') + 1
    # start_id = 1211

    end_id = 100001

    input_thread_instance = Thread(target=input_thread)
    input_thread_instance.start()

    try:
        with ThreadPoolExecutor(max_workers=1) as executor:
            future_to_id = {executor.submit(process_book, book_id): book_id for book_id in range(start_id, end_id)}

            for future in as_completed(future_to_id):
                if stop_requested:
                    break  # Detiene el proceso si se solicitó

                book_id = future_to_id[future]
                try:
                    data = future.result()
                    if data is not None:
                        print(f"Procesado libro con ID: {data}")
                except Exception as e:
                    print(f"Error procesando libro con ID {book_id}: {e}")

    except KeyboardInterrupt:
        print("Proceso interrumpido por el usuario. Finalizando...")

    input_thread_instance.join()  # Espera a que el hilo de input termine

if __name__ == '__main__':
    main()
