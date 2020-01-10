import requests
from bs4 import BeautifulSoup
import pandas as pd


def search_url(**kwargs):
    vendor = 'ford'
    model = 'focus'
    url = f"https://www.avito.ru/voronezh/avtomobili/{vendor}/{model}"
    return url




def get_avito_offers_urls():
    u = search_url()
    response = requests.get(u)
    soup = BeautifulSoup(response.content.decode('utf-8'), 'html.parser')

    offer_url = soup.find_all('a', {"itemprop": "url"})
    offer_urls = []
    for i in range(len(offer_url)):

        offer_urls.append("https://www.avito.ru" + offer_url[i].get('href'))

    return offer_urls



def avito_offer(offer_url):
    response = requests.get(offer_url)
    soup = BeautifulSoup(response.content.decode('utf-8'), 'html.parser')
    avito_offer_text = "Цена: " + (soup.find("span", {"class": "js-item-price"}).text) + " " + soup.find("ul",{"class": "item-params-list"}).text
    params = soup.find_all("li",{"class": "item-params-list-item"})

    avito_offer_dict = { 'bodyType': params[9].contents[2],
                         'brand': params[0].contents[2],
                         'color': None,
                         'fuelType': params[11].contents[2],
                         'modelDate': None,
                         'name': None,
                         'numberOfDoors': None,
                         'productionDate': params[4].contents[2],
                         'vehicleTransmission': params[12].contents[2],
                         'price': (soup.find("span", {"class": "js-item-price"}).text),
                         'url': offer_url,
                         'engineDisplacement': None,
                         'enginePower': None,

                         }
    return print(avito_offer_dict)


def avito_dataframe():
    offers = get_avito_offers_urls()
    list_autos = []
    for offer_url in offers:
        offer_data = avito_offer(offer_url)
        list_autos.append(offer_data)
    autos = pd.DataFrame(list_autos)
    autos['site'] = 'Avito'
    return autos







if __name__ == '__main__':

    print(avito_dataframe())