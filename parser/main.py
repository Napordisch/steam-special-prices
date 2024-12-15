import steam_parser
import zaka_zaka_parser
import gabestore_parser
import steampay_parser
import db

data_base = db.DataBase('db', 'user', 'user_password', 'game_info')
games_with_prices = steam_parser.get_top_games_on_steam_with_special_prices()
for game in games_with_prices:
    game.zaka_zaka_price = zaka_zaka_parser.find_game_price(game.name)
    game.gabe_store_price = gabestore_parser.find_game_price(game.name)
    game.steam_pay_price = steampay_parser.find_game_price(game.name)
    data_base.update_game_prices(game)
    print("Updated info about game:", end="\t")
    data_base.add_game_image(game)
    print(game.name,
          game.steam_price,
          game.zaka_zaka_price,
          game.steam_pay_price,
          game.steam_account_price,
          game.gabe_store_price,
          game.ggsell_price,
          sep="\t")