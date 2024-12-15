import requests
from bs4 import BeautifulSoup
import re


def find_game_price(name: str) -> float | None:
    formatted_name = '-'.join(
        map(lambda word: word.lower(),
            re.findall("(\\w+)", name))
    )
    game_url = "https://gabestore.ru/game/" + formatted_name
    page = requests.get(game_url).text
    page_as_soup = BeautifulSoup(page, 'html.parser')
    price_class = "b-card__price-currentprice"
    price_element = page_as_soup.find(class_=price_class)
    if price_element is None:
        print(f"{name} not found in GabeStore")
        return None
    print(f"Found {name} in GabeStore")
    return float(price_element.text.strip().split()[0].replace(",", "."))

if __name__ == "__main__":
    print(find_game_price("Legacy of Kain: Soul Reaver 1-2 Remastered"))