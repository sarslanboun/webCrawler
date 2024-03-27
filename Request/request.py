
import requests
from bs4 import BeautifulSoup
from requests import Response
import logging


class Request:

    def __init__(self):
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/122.0.0.0 Safari/537.36"
        }
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler = logging.FileHandler('requests.log')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    @staticmethod
    def request(url: str, counter = 0) -> Response | None:
        try:
            counter += 1
            response = requests.get(url, headers=Request().header)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            if counter < 4:
                Request.request(url, counter)
                Request().logger.error(f"Request failed for URL: {url}. Error: {e}. Trying again {counter} times.")
            else:
                Request().logger.error(f"Request failed for URL: {url}. Error: {e}")
                return None

    @staticmethod
    def get_soup(url: str) -> BeautifulSoup | None:
        response = Request.request(url)
        if response is not None:
            soup_result = BeautifulSoup(response.content, "html.parser")
            return soup_result
        else:
            return None
