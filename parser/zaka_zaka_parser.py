import requests
from bs4 import BeautifulSoup
import utilities

def find_game_price_and_link(name: str) -> tuple[float, str] | tuple[None,None]:
    formatted_name = utilities.to_kebab_case(name)
    game_url = "https://zaka-zaka.com/game/" + formatted_name
    page = requests.get(game_url).text
    page_as_soup = BeautifulSoup(page, 'html.parser')
    price_class = "price"
    price_element = page_as_soup.find(class_=price_class)
    if price_element is None:
        print(f"{name} not found in zaka-zaka")
        return None, None
    print(f"Found {name} in zaka-zaka")
    try:
        return float(price_element.text.strip().split()[0].replace(",", ".")), game_url
    except ValueError:
        return None, None

if __name__ == "__main__":
    print(find_game_price_and_link("Grpaveyard Keeer"))