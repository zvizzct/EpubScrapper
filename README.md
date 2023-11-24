# Python Book Scraper Program

## Overview

This Python program is designed to scrape book details from a specific website and save the data in a JSON file. It leverages multithreading to process multiple books concurrently and provides functionality to stop the process on user command.

## Features

- **Concurrent Scraping**: Utilizes `ThreadPoolExecutor` for concurrent scraping.
- **Interruptible Process**: Allows the user to stop the process with an input command.
- **Data Extraction**: Extracts various book details like title, authors, genres, and more.
- **JSON Data Storage**: Saves the scraped data into a JSON file, maintaining order by book ID.

## Structure

- `main.py`: Main script to initiate the scraping process.
- `logic/extractors.py`: Contains functions to extract different book details from HTML content.
- `logic/get_json_book.py`: Handles the process of fetching and parsing HTML content from the web.
- `logic/save_to_json.py`: Manages the saving of book data into a JSON file.
- `clients/scraperapi_client.py`: Wrapper for making requests to the website with ScraperAPI.

## Usage

1. **Starting the Program**: Run `main.py` to start the scraping process.
2. **Stopping the Program**: Input 's' in the console to stop the process.

## Dependencies

- BeautifulSoup
- requests
- concurrent.futures
- threading

## Configuration

- Set the `SCRAPER_API_KEY` in `config/settings` for ScraperAPI access.
- Modify the `start_id` and `end_id` in `main.py` to set the range of book IDs to scrape.
