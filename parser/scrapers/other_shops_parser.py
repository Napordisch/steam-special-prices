import requests
import utilities
from bs4 import BeautifulSoup


def find_game_price_and_link(name: str, shop: str) -> tuple[float, str] | \
                                                      tuple[None, None]:
    shop_url = {"zaka_zaka": "https://zaka-zaka.com/",
                "steam_pay": "https://steampay.com/",
                "gabe_store": "https://gabestore.ru/"}
    price_classes = {"zaka_zaka": "price",
                     "steam_pay": "product__current-price",
                     "gabe_store": "b-card__price-currentprice"}
    formatted_name = utilities.to_kebab_case(name)
    game_url = shop_url[shop] + 'game/' + formatted_name
    page = requests.get(game_url).text
    page_as_soup = BeautifulSoup(page, 'html.parser')
    price_class = price_classes[shop]
    price_element = page_as_soup.find(class_=price_class)
    if price_element is None:
        print(f"{name} not found in {shop}")
        return None, None
    print(f"Found {name} in {shop}")
    try:
        return float(
            price_element.text.strip().split()[0].replace(",", ".")), game_url
    except ValueError:
        return None, None
