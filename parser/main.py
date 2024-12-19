import db
import time
from scrapers import steam_parser
from scrapers.other_shops_parser import find_game_price_and_link
import os

DB_NAME = os.environ.get("DB_NAME")
DB_LOGIN = os.environ.get("DB_LOGIN")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_HOST = os.environ.get("DB_HOST")
data_base = db.DataBase(DB_HOST, DB_LOGIN, DB_PASSWORD, DB_NAME)
while True:
    games_with_prices = steam_parser.get_top_games_on_steam_with_special_prices()
    place_in_top = 1
    for game in games_with_prices:

        (game.zaka_zaka_price, game.zaka_zaka_link), (game.gabe_store_price, game.gabe_store_link), (game.steam_pay_price, game.steam_pay_link) = \
        find_game_price_and_link(game.name, "zaka_zaka"), find_game_price_and_link(game.name, "gabe_store"), find_game_price_and_link(game.name, "steam_pay")

        data_base.update_game_prices(game, place_in_top)
        print("Updated info about game:", end="\t")
        data_base.add_game_image(game)
        data_base.add_game_name(game)
        data_base.add_game_links(game)
        print(game.name,
              game.steam_price,
              game.zaka_zaka_price,
              game.steam_pay_price,
              game.steam_account_price,
              game.gabe_store_price,
              sep="\t")
        place_in_top += 1

    print("parsing finished, waiting for the next attempt...")
