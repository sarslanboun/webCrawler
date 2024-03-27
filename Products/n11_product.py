import logging

from requests import RequestException

from Products.base_product_parameters import BaseProductMethods
from Request.request import Request


class N11Product(BaseProductMethods):
    def __init__(self, url):
        self.url = url
        try:
            self.soup = Request.get_soup(url)
        except RequestException as e:
            error_msg = f"Failed to fetch content from {url}: {e}"
            logging.error(error_msg)
            print(error_msg)
            self.soup = None

    def title(self):
        if self.soup:
            try:
                return self.soup.find("h1", attrs={"class": "proName"}).text.strip()
            except AttributeError:
                error_msg = "Failed to extract title. For this url:", self.url
                logging.error(error_msg)
                # print(error_msg)
        return None

    def price(self):
        if self.soup:
            try:
                return self.soup.find("input", attrs={"id": "skuPrice"}).get("value").strip()
            except AttributeError:
                error_msg = "Failed to extract price. For this url:", self.url
                logging.error(error_msg)
                # print(error_msg)
        return None

    def price_without_discount(self):
        if self.soup:
            try:
                return self.soup.find("input", attrs={"id": "skuOldPrice"}).get("value").strip()
            except AttributeError:
                error_msg = "Failed to extract price without discount. For this url:", self.url
                logging.error(error_msg)
                # print(error_msg)
        return None

    def main_image_url(self):
        if self.soup:
            try:
                return self.soup.find("div", attrs={"class": "imgObj"}).find("img").get("data-original")
            except AttributeError:
                error_msg = "Failed to extract main image URL. For this url:", self.url
                logging.error(error_msg)
                # print(error_msg)
        return None

    def image_urls(self):
        if self.soup:
            try:
                image_url_elements = self.soup.find("div", attrs={"id": "thumbSlider"}).find_all("div", attrs={
                    "class": "unf-p-thumbs-item"})
                image_urls = []
                for image_url in image_url_elements:
                    image_urls.append(image_url.get("data-full"))
                return image_urls
            except AttributeError:
                error_msg = "Failed to extract image URLs. For this url:", self.url
                logging.error(error_msg)
                # print(error_msg)
        return []

    def rating_score(self):
        if self.soup:
            try:
                return self.soup.find("div", attrs={"class": "ratingCont"}).find("strong").text.strip()
            except AttributeError:
                error_msg = "Failed to extract rating score. For this url:", self.url
                logging.error(error_msg)
                # print(error_msg)
        return None

    def rating_count(self):
        if self.soup:
            try:
                return self.soup.find("a", attrs={"id": "readReviews"}).find("span").text.strip()
            except AttributeError:
                error_msg = "Failed to extract rating count. For this url:", self.url
                logging.error(error_msg)
                # print(error_msg)
        return None

    def review_count(self):
        return None
