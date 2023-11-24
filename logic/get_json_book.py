
from bs4 import BeautifulSoup
from numpy import number
from clients.scraperapi_client import ScraperAPI
from .extractors import (
    extract_title, extract_authors, extract_genres, 
    extract_synopsis, extract_image, extract_votes, 
    extract_publication_date, extract_magnet_link, extract_book_id, extract_number_of_pages, extract_language
)

def scrape_book_details(url):
    client = ScraperAPI()
    response = client.get(url)
    if not response.ok:
        print('Error en la solicitud:', response.text)
        return None

    soup = BeautifulSoup(response.content, 'html.parser')

    # Usando las funciones de extracción
    title = extract_title(soup)
    authors = extract_authors(soup)
    genres = extract_genres(soup)
    synopsis = extract_synopsis(soup)
    votes = extract_votes(soup)
    publication_date = extract_publication_date(soup)
    magnet_link = extract_magnet_link(soup)
    book_id = extract_book_id(url)
    image_url = extract_image(soup)
    number_of_pages = extract_number_of_pages(soup)
    language = extract_language(soup)

    book_details = {
        'id': int(book_id),
        'title': title,
        'authors': authors,
        'genres': genres,
        'synopsis': synopsis,
        'votes': int(votes),
        'publication_date': publication_date,
        'magnet_link': magnet_link,
        'image_url': image_url,
        'number_of_pages': int(number_of_pages),
        'language': language

    }

    return book_details
