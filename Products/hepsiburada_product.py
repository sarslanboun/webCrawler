import logging

from requests import RequestException

from Products.base_product_parameters import BaseProductMethods
from Request.request import Request


class HepsiburadaProduct(BaseProductMethods):
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
                return self.soup.find("h1", attrs={"id": "product-name"}).text.strip()
            except AttributeError:
                error_msg = "Failed to extract title. For this url:", self.url
                logging.error(error_msg)
                # print(error_msg)
        return None

    def price(self):
        if self.soup:
            try:
                return self.soup.find("span", attrs={"id": "pageVariantPrice"}).text.strip()
            except AttributeError:
                error_msg = "Failed to extract price. For this url:", self.url
                logging.error(error_msg)
                # print(error_msg)
        return None

    def price_without_discount(self):
        if self.soup:
            try:
                return self.soup.find("del", attrs={"id": "originalPrice"}).text.strip()
            except AttributeError:
                error_msg = "Failed to extract price without discount. For this url:", self.url
                logging.error(error_msg)
                # print(error_msg)
        return None

    def main_image_url(self):
        if self.soup:
            try:
                return self.soup.find("img", attrs={"class": "product-image"}).get("src")
            except AttributeError:
                error_msg = "Failed to extract main image URL. For this url:", self.url
                logging.error(error_msg)
                # print(error_msg)
        return None

    def image_urls(self):
        if self.soup:
            try:
                image_url_elements = self.soup.find("div", attrs={"id": "productDetailsCarousel"}).find_all("img", attrs={
                    "class": "product-image"})
                image_urls = []
                for image_url in image_url_elements:
                    if (image_url.get("data-src") is not None) and (image_url.get("data-src") != ""):
                        image_urls.append(image_url.get("data-src"))
                if (self.main_image_url()) not in image_urls:
                    image_urls.append(self.main_image_url())
                return image_urls
            except AttributeError:
                error_msg = "Failed to extract image URLs. For this url:", self.url
                logging.error(error_msg)
                # print(error_msg)
        return []

    def rating_score(self):
        if self.soup:
            try:
                return self.soup.find("span", attrs={"itemprop": "ratingValue"}).text.strip()
            except AttributeError:
                error_msg = "Failed to extract rating score. For this url:", self.url
                logging.error(error_msg)
                # print(error_msg)
        return None

    def rating_count(self):
        if self.soup:
            try:
                return self.soup.find("div", attrs={"id": "comments-container"}).find("span").text.strip()
            except AttributeError:
                error_msg = "Failed to extract rating count. For this url:", self.url
                logging.error(error_msg)
                # print(error_msg)
        return None

    def review_count(self):
        return None
