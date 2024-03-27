import openpyxl

from Mail.email_notifier import EmailNotifier
from Utilities.utilities import product_urls_txt_to_list, \
    create_product, products_to_csv, products_to_json, products_to_xlsx

if __name__ == '__main__':
    # txt dosyası açılır
    product_urls = open("urls.txt", "r")

    # txt dosyası liste haline getirilir
    url_list = product_urls_txt_to_list(product_urls)

    # productlardan birine class olur
    products = create_product(url_list)

    # csv türünden sonuç döner
    csv_result = products_to_csv(products)

    # sonucu bas
    print("---csv")
    print(csv_result.read())
    print("---csv")

    # json türünden sonuç döner
    json_result = products_to_json(products)

    # sonucu bas
    print("---json")
    print(json_result.read())
    print("---json")

    # xlsx türünden sonuç döner
    xlsx_result = products_to_xlsx(products)

    # xlsx dosyasını kaydet
    xlsx_result.save("products.xlsx")

    # sonucu bas
    print("---excel")
    wb_read = openpyxl.load_workbook("products.xlsx")
    ws_read = wb_read.active
    for row in ws_read.iter_rows(values_only=True):
        print(row)
    print("---excel")


    # mail gönderir
    email_notifier = EmailNotifier("serdar.arslan.sender.mail@gmail.com", "orom igml jozg elmq")
    email_notifier.send_email("s.arslan1696@gmail.com", "topic", "body", "products.xlsx")
