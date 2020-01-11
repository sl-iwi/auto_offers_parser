import requests
from bs4 import BeautifulSoup
import pandas as pd


def search_url(**kwargs):
    location = 'voronezh'
    vendor = 'ford'
    model = 'focus'
    url = f"https://www.avito.ru/{location}/avtomobili/{vendor}/{model}"
    return url




def get_avito_offers():
    u = search_url()
    response = requests.get(u)
    soup = BeautifulSoup(response.content.decode('utf-8'), 'html.parser')
    offers = soup.findAll('div', {'class': 'item__line'})
    list_autos = []
    for i in range(len(offers)):
        # Mileage, bodytype, EnginePower, fueltype,  vehicleTransmission
        keys = ['mileage', 'EnginePower', 'bodytype' 'privod','fueltype']
        params = (offers[i].findChild('div', {'class', 'specific-params specific-params_block'}).text).split(',')
        price = offers[i].findChild('span', {'class', 'price price_highlight'})




        list_autos.append(params)
    return list_autos

if __name__ == '__main__':

    print(get_avito_offers ())