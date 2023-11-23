
import requests
from config.settings import SCRAPER_API_KEY

class ScraperAPI:
    def __init__(self):
        self.api_endpoint = 'http://api.scraperapi.com'
        self.api_key = SCRAPER_API_KEY

    def get(self, url, **kwargs):
        payload = {
            'api_key': self.api_key,
            'url': url,
            **kwargs  # Esto permite agregar parámetros adicionales como 'render'
        }
        response = requests.get(self.api_endpoint, params=payload)
        return response
