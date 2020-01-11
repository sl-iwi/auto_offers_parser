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
    for data in offers:
        # Mileage, bodytype, EnginePower, fueltype,  vehicleTransmission
        keys = ['mileage', 'EnginePower', 'bodytype', 'privod','fueltype']
        values = (data.findChild('div', {'class': 'specific-params specific-params_block'}).text).split(',')
        params = dict(zip(keys, values))

        url = 'https://avito.ru' + data.findChild('a', {'class': 'snippet-link'}, href = True)['href']
        params.update({'url': url})


        price = data.findChild('span', {'itemprop': 'price'})
        if price is not None:
            params.update({'price': price.text})

        list_autos.append(params)
    autos = pd.DataFrame(list_autos)
    autos['site']='Avito'
    return autos


if __name__ == '__main__':

    print(get_avito_offers ())