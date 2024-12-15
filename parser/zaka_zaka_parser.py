import requests
from bs4 import BeautifulSoup
import re

# using search results
# def find_game_price(name) -> float | None:
#     page = requests.get(f"https://zaka-zaka.com/search/ask/{name}/sort/name.asc").text
#     page_as_soup = BeautifulSoup(page, 'html.parser')
#     game_block_as_soup = BeautifulSoup(str(page_as_soup.find(class_="game-block")), 'html.parser')
#     if game_block_as_soup.find(class_ ="game-block-name") is None:
#         return None
#     if game_block_as_soup.find(class_ = "game-block-name").text == name:
#         print(f"found {name} in zaka-zaka")
#         return float(game_block_as_soup.find(class_ = "game-block-price").text.strip().split()[0].replace(",", "."))
#     else:
#         print(f'{name} not found in zaka-zaka')
#         return None

#using page
def find_game_price(name: str) -> float | None:
    formatted_name = '-'.join(
        map(lambda word: word.lower(),
            re.findall("(\\w+)", name))
    )
    game_url = "https://zaka-zaka.com/game/" + formatted_name
    page = requests.get(game_url).text
    page_as_soup = BeautifulSoup(page, 'html.parser')
    price_class = "price"
    price_element = page_as_soup.find(class_=price_class)
    if price_element is None:
        print(f"{name} not found in zaka-zaka")
        return None
    print(f"Found {name} in zaka-zaka")
    return float(price_element.text.strip().split()[0].replace(",", "."))

if __name__ == "__main__":
    print(find_game_price("Graveyard Keeper"))