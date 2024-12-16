import steam_parser
import zaka_zaka_parser
import gabestore_parser
import steampay_parser
import db

data_base = db.DataBase('db', 'user', 'user_password', 'game_info')
games_with_prices = steam_parser.get_top_games_on_steam_with_special_prices()
place_in_top = 1
for game in games_with_prices:
    game.zaka_zaka_price, game.zaka_zaka_link = zaka_zaka_parser.find_game_price_and_link(game.name)
    game.gabe_store_price, game.gabe_store_link = gabestore_parser.find_game_price_and_link(game.name)
    game.steam_pay_price, game.steam_pay_link = steampay_parser.find_game_price_and_link(game.name)
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