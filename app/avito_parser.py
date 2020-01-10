import requests
from bs4 import BeautifulSoup
import pandas as pd


avito_autos = pd.DataFrame(
    columns=['brand', 'model', 'bodytype', 'price', 'productionDate', 'mileage', 'motor', 'motortype', 'gear', 'pts',
             'owners', 'location', 'vin', 'reg_number', 'wrecked'
             ])

def get_avito_offers_urls(vendor, model):
    u = f"https://www.avito.ru/voronezh/avtomobili/{vendor}/{model}"
    response = requests.get(u)
    soup = BeautifulSoup(response.content.decode('utf-8'), 'html.parser')

    offer_url = soup.find_all('a', {"itemprop": "url"})
    offer_urls = []
    for i in offer_url:

        offer_urls.append(offer_url[i].get('href'))

    return offer_urls



def avito_offer(offer_url):
    response = requests(offer_url)
    soup = BeautifulSoup(response.content.decode('utf-8'), 'html.parser')
    avito_offer = "Цена: " + (soup.find("span", {"class": "js-item-price"}).text) + " " + soup.find("ul",{"class": "item-params-list"}).text
    return avito_offer


