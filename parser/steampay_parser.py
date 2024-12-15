import requests
from bs4 import BeautifulSoup
import re

def find_game_price(name: str) -> float | None:
    formatted_name = '-'.join(
        map(lambda word: word.lower(),
            re.findall("(\\w+)", name))
    )
    game_url = "https://steampay.com/game/" + formatted_name
    page = requests.get(game_url).text
    page_as_soup = BeautifulSoup(page, 'html.parser')
    price_class = "product__current-price"
    price_element = page_as_soup.find(class_=price_class)
    if price_element is None:
        print(f"{name} not found in steampay")
        return None
    print(f"Found {name} in steampay")
    try:
        return float(price_element.text.strip().split()[0].replace(",", "."))
    except ValueError:
        return None

if __name__ == "__main__":
    print(find_game_price("Days Gone"))