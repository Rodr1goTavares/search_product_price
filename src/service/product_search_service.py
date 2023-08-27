import datetime

import requests
from bs4 import BeautifulSoup

date = str(datetime.date.today())

class ProductSearchService:
    @staticmethod
    def search_product_in_mercadolivre(product_name):
        url = "https://lista.mercadolivre.com.br/"+ product_name +"#D[A:"+ product_name +"]"
        try:
            search_result = requests.get(url).content
            soup = BeautifulSoup(search_result, 'html.parser')
            name = soup.find('h2', class_='ui-search-item__title shops__item-title').get_text()
            price = soup.find('span', class_='andes-money-amount__fraction').get_text()
            result = "Store: Mercado Livre" + "\nName: " + name + "\nPrice: R$" + price + "\nDate: " + date + "\nLink: " + url + "\n----------"
            print(result)
            return (result)
        except Exception as error:
            print("Error to search product in Mercado Livre: " + str(error))

    @staticmethod
    def search_product_In_amazon(product_name):
        url = "https://www.amazon.com.br/s?k=" + product_name + "&__mk_pt_BR=ÅMÅŽÕÑ&crid=3ONOUBRSEH5MH&sprefix=" + product_name + "+%2Caps%2C229&ref=nb_sb_noss_2"
        try:
            search_result = requests.get(url).content
            soup = BeautifulSoup(search_result, 'html.parser')
            name = soup.find('span', class_='a-size-base-plus a-color-base a-text-normal').get_text()
            price = soup.find('span', class_='a-price-whole').get_text()
            result = "Store: Amazon" + "\nName: " + name + "\nPrice: R$" + price + "\nDate: " + date + "\nLink: " + url +  "\n----------"
            print(result)
            return (result)
        except Exception as error:
            print("Error to search product in Amazon: " + str(error))