
import requests
from bs4 import BeautifulSoup
import pandas as pd



def search_url(**kwargs):
    location = 'voronezh'
    vendor = 'ford'
    model = 'focus'
    url = f"https://auto.ru/{location}/cars/{vendor}/{model}/used"
    return url


# this func returns dataframe with offers.
def get_autoru_offers():
    u = search_url()

    response = requests.get(u)
    soup = BeautifulSoup(response.content.decode('utf-8'), "html.parser")
    listitems = soup.find_all("div", {"class": "ListingItem-module__container ListingCars-module__listingItem"}) #list of offers 1st page

    list_autos = []
    for i in range(len(listitems)):
        offer = {}
        # parse ['bodyType', 'brand', 'color', 'fuelType', 'modelDate', 'name', 'productionDate', 'vehicleTransmission', 'price', 'url', 'engineDisplacement', 'enginePower', ]
        for meta in listitems[i].find_all("meta"):
            key = meta.get('itemprop')
            value = meta.get('content')
            offer.update({key: value})
        # parse mileage
        offer.update({'mileage': listitems[i].findChild('div', {'class': 'ListingItem-module__kmAge'}).text})

        list_autos.append(offer)

    autos = pd.DataFrame(list_autos)
    # Правим датасет
    autos = autos.drop(['image', 'availability', 'priceCurrency', 'numberOfDoors', 'vehicleConfiguration'], 1)
    autos['site']='Auto.ru'

    return print(autos)







if __name__ == '__main__':

    print(get_autoru_offers())

