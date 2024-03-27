import json
import logging

from requests import RequestException

from Products.base_product_parameters import BaseProductMethods
from Request.request import Request


class TrendyolProduct(BaseProductMethods):
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
                return self.soup.find("h1").find("span").text.strip()
            except AttributeError:
                error_msg = "Failed to extract title. For this url:", self.url
                logging.error(error_msg)
                # print(error_msg)
        return None

    def price(self):
        if self.soup:
            try:
                return (self.soup.find("div", attrs={"class": "featured-prices"})
                        .find("span", attrs={"class": "prc-dsc"}).text.strip())
            except AttributeError:
                error_msg = "Failed to extract price. For this url:", self.url
                logging.error(error_msg)
                # print(error_msg)
        return None

    def price_without_discount(self):
        if self.soup:
            try:
                return self.soup.find("div", attrs={"class": "featured-prices"}).find("span", attrs={
                    "class": "prc-org"}).text.strip()
            except AttributeError:
                error_msg = "Failed to extract price without discount. For this url:", self.url
                logging.error(error_msg)
                # print(error_msg)
        return None

    def main_image_url(self):
        # if self.soup:
        #     try:
        #         script = self.soup.find("script", attrs={"type": "application/ld+json"})
        #         script_json = json.loads(script[0])
        #         image_list = script_json["image"]
        #         return image_list[0]
        #     except AttributeError and KeyError and TypeError:
        #         error_msg = "Failed to extract main image URL."
        #         logging.error(error_msg)
        #         # print(error_msg)
        # return None
        return None

    def image_urls(self):
        # if self.soup:
        #     try:
        #         script = self.soup.find("script", attrs={"type": "application/ld+json"})
        #         script_json = json.loads(script[0])
        #         image_list = script_json["image"]
        #         return image_list
        #     except AttributeError and KeyError and TypeError:
        #         error_msg = "Failed to extract image URLs."
        #         logging.error(error_msg)
        #         # print(error_msg)
        # return []
        return []

    def rating_score(self):
        # if self.soup:
        #     try:
        #         script = self.soup.find("script", attrs={"type": "application/ld+json"})
        #         script_json = json.loads(script[0])
        #         rating_score = script_json["aggregateRating"]["ratingValue"]
        #         return rating_score
        #     except AttributeError and KeyError and TypeError:
        #         error_msg = "Failed to extract rating score."
        #         logging.error(error_msg)
        #         # print(error_msg)
        # return None
        return None

    def rating_count(self):
        # if self.soup:
        #     try:
        #         script = self.soup.find("script", attrs={"type": "application/ld+json"})
        #         script_json = json.loads(script[0])
        #         rating_count = script_json["aggregateRating"]["ratingCount"]
        #         return rating_count
        #     except AttributeError and KeyError:
        #         error_msg = "Failed to extract rating count."
        #         logging.error(error_msg)
        #         # print(error_msg)
        # return None
        return None

    def review_count(self):
        # if self.soup:
        #     try:
        #         script = self.soup.find("script", attrs={"type": "application/ld+json"})
        #         script_json = json.loads(script[0])
        #         review_count = script_json["aggregateRating"]["reviewCount"]
        #         return review_count
        #     except AttributeError and KeyError and TypeError:
        #         error_msg = "Failed to extract rating count."
        #         logging.error(error_msg)
        #         # print(error_msg)
        # return None
        return None
