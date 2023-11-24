
def extract_title(soup):
    title_element = soup.find('div', class_='det_titulo')
    return title_element.text.strip() if title_element else ""

def extract_authors(soup):
    authors = {}
    authors_table = soup.find('div', string=lambda text: text and 'Autores' in text).find_next('table')
    if authors_table:
        for row in authors_table.find_all('tr'):
            role = row.find('div', class_='label').text.strip()
            name = row.find('td', class_='negrita txt_azul').text.strip()
            authors[role.lower()] = name
    return authors


def extract_genres(soup):
    genres = {}
    genres_table = soup.find('div', string=lambda text: text and 'Géneros' in text).find_next('table')
    if genres_table:
        for row in genres_table.find_all('tr'):
            genre_type = row.find('div', class_='label').text.strip()
            genre_name = row.find_all('td')[1].text.strip()
            if genre_type in genres:
                if isinstance(genres[genre_type], list):
                    genres[genre_type].append(genre_name)
                else:
                    genres[genre_type] = [genres[genre_type], genre_name]
            else:
                genres[genre_type] = genre_name
    return genres

def extract_synopsis(soup):
    synopsis_element = soup.find('div', class_='ali_justi')
    synopsis = synopsis_element.span.text.strip() if synopsis_element else ""
    return synopsis

def extract_image(soup):
    image_element = soup.find('img', id='portada')
    return image_element['src']

def extract_votes(soup):
    votes_element = soup.find('span', id='msgVotos')
    return votes_element.text.strip().split()[0] if votes_element else ""

def extract_publication_date(soup):
    publication_date_element = soup.find('td', string='Publicado en:')
    return publication_date_element.find_next_sibling('td').text.strip() if publication_date_element else ""

def extract_magnet_link(soup):
    magnet_link_element = soup.find('a', id='en_desc')
    return magnet_link_element['href'] if magnet_link_element else ""

def extract_book_id(url):
    return url.split('/')[-1]

def extract_number_of_pages(soup):
    pages_element = soup.find('td', string=lambda text: text and 'Páginas:' in text)
    if pages_element and pages_element.find_next_sibling('td'):
        pages_text = pages_element.find_next_sibling('td').text.strip()
        return ''.join(filter(str.isdigit, pages_text))
    return "No disponible"

def extract_language(soup):
    language_element = soup.find('span', class_='txt_blanco')
    return language_element.text.strip() if language_element else "Idioma no disponible"