
import requests
from bs4 import BeautifulSoup
import pandas as pd



def search_url(**kwargs):
    vendor = 'ford'
    model = 'focus'
    url = f"https://auto.ru/voronezh/cars/{vendor}/{model}/used"
    return url




def get_autoru_offers(vendor,model):
    u = search_url()

    response = requests.get(u)
    soup = BeautifulSoup(response.content.decode('utf-8'), "html.parser")
    listitems = soup.find_all("div", {"class": "ListingItem-module__container ListingCars-module__listingItem"}) #list of offers 1st page

    list_autos = []
    for i in range(len(listitems)):
        offer = {}
        for meta in listitems[i].find_all("meta"):
            key = meta.get('itemprop')
            value = meta.get('content')
            offer.update({key: value})
        list_autos.append(offer)

    autos = pd.DataFrame(list_autos)
    # Правим датасет
    autos = autos.drop('image', 1 )
    autos = autos.drop('availability', 1)
    autos = autos.drop('priceCurrency', 1)

    return print(autos)







if __name__ == '__main__':

    print(get_autoru_offers('ford','focus'))

