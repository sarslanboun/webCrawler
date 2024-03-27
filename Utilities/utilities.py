import csv
import json
from urllib.parse import urlparse

import openpyxl

from Products.hepsiburada_product import HepsiburadaProduct
from Products.n11_product import N11Product
from Products.trendyol_product import TrendyolProduct


# txt file'ı listeye çevirir
def product_urls_txt_to_list(txt_file):
    lines = []
    for line in txt_file:
        lines.append(line.strip())
    return lines


# liste içindeki urlleri product türlerine çevirir
def create_product(url_list):
    products = []
    for url in url_list:
        product = None
        if urlparse(url).netloc.__eq__("www.trendyol.com"):
            product = TrendyolProduct(url)

        elif urlparse(url).netloc.__eq__("www.hepsiburada.com"):
            product = HepsiburadaProduct(url)

        elif urlparse(url).netloc.__eq__("www.n11.com"):
            product = N11Product(url)
        else:
            print("URL does not include any retailer." , url)
            continue
        products.append(product)
    return products


# productlar olan listeyi csv sonucuna çevirir
def products_to_csv(products):
    csv_results = open("csv_results", "w+", newline="", encoding='utf-8')

    for product in products:
        if product:
            title = product.title()
            price = product.price()
            price_without_discount = product.price_without_discount()
            main_image_url = product.main_image_url()
            image_urls = product.image_urls()
            rating_score = product.rating_score()
            rating_count = product.rating_count()
            review_count = product.review_count()

            csv.writer(csv_results).writerow(
                [title, price, price_without_discount, main_image_url, image_urls, rating_score, rating_count,
                 review_count])

    csv_results.seek(0)
    return csv_results


# productlar olan listeyi json sonucuna çevirir
def products_to_json(products):
    products_list = []
    json_results = open("csv_results", "w+")

    for product in products:
        if product:
            product_info = {'title': product.title(), 'price': product.price(),
                            'price_without_discount': product.price_without_discount(),
                            'main_image_url': product.main_image_url(), 'image_urls': product.image_urls(),
                            'rating_score': product.rating_score(), 'rating_count': product.rating_count(),
                            'review_count': product.review_count()}

            products_list.append(product_info)

    json.dump(products_list, json_results)
    json_results.seek(0)
    return json_results

# productlar olan listeyi xlsx sonucuna çevirir
def products_to_xlsx(products):
    wb = openpyxl.Workbook()
    ws = wb.active

    headers = ['title', 'price', 'price_without_discount', 'main_image_url', 'image_urls', 'rating_score',
               'rating_count', 'review_count']
    ws.append(headers)
    for product in products:
        if product:
            product_info = {'title': product.title(), 'price': product.price(),
                            'price_without_discount': product.price_without_discount(),
                            'main_image_url': product.main_image_url(), 'image_urls': ', '.join(product.image_urls()),
                            'rating_score': product.rating_score(), 'rating_count': product.rating_count(),
                            'review_count': product.review_count()}

            rows = [product_info.get(key, "") for key in headers]  # somehow works
            ws.append(rows)

    return wb
