
import requests
from bs4 import BeautifulSoup

def get_autoru_offers(vendor,model):
    u = f"https://auto.ru/voronezh/cars/{vendor}/{model}/used"
    autos = []
    response = requests.get(u)
    soup = BeautifulSoup(response.content.decode('utf-8'), "html.parser")
    listitems = soup.find_all("div", {"class": "ListingItem-module__container ListingCars-module__listingItem"}) #list of offers 1st page
    for i in range(len(listitems)):
         offer = []
         for meta in listitems[i].find_all("meta"):
             offer.append(meta.attrs)
         autos.append(offer)

    return autos





if __name__ == '__main__':

    print(get_autoru_offers('ford','focus'))

