# main.py

from concurrent.futures import ThreadPoolExecutor, as_completed
from logic.get_json_book import scrape_book_details
from logic.save_to_json import save_book_info, get_last_saved_id

def process_book(book_id):
    url = f'https://www.epublibre.org/libro/detalle/{book_id}'
    book_info = scrape_book_details(url)
    if book_info:
        save_book_info(book_info, 'books_data.json')
    return book_id

def main():
    start_id = get_last_saved_id('books_data.json') + 1
    end_id = 100001

    try:
        with ThreadPoolExecutor(max_workers=20) as executor:
            future_to_id = {executor.submit(process_book, book_id): book_id for book_id in range(start_id, end_id)}

            for future in as_completed(future_to_id):
                book_id = future_to_id[future]
                try:
                    data = future.result()
                    print(f"Procesado libro con ID: {data}")
                except Exception as e:
                    print(f"Error procesando libro con ID {book_id}: {e}")

    except KeyboardInterrupt:
        print("Proceso interrumpido por el usuario. Finalizando...")

if __name__ == '__main__':
    main()
