from flask import Flask, render_template, jsonify, send_from_directory
from db import query_db

app = Flask(__name__, static_folder='static')

@app.route('/static/<path:filename>')
def send_static(filename):
    return send_from_directory('static', filename)

@app.route('/')
def show_all_games_page():
    return send_from_directory('static', "main_page.html")

@app.route('/all-games-prices')
def get_games_prices():
    games_with_prices_and_images = query_db("SELECT * FROM game_prices ORDER by place_in_top ASC")
    for game in games_with_prices_and_images:
        image_link_dict = query_db(f"SELECT image_link FROM game_images WHERE id = \"{game['id']}\"")[0]
        shop_links = query_db(f"SELECT zaka_zaka_link, steam_pay_link, gabe_store_link FROM game_links WHERE id = \"{game['id']}\"")[0]
        game.update(image_link_dict)
        game.update(shop_links)
    return jsonify(games_with_prices_and_images)

@app.route('/all-game-names')
def get_all_game_names():
    return(jsonify(list(map(
        lambda game_id_tuple: game_id_tuple["id"],
        query_db("SELECT id FROM game_prices ORDER by place_in_top ASC")
    ))))

@app.route('/game-info/<game_id>')
def get_game_with_prices(game_id):
    game = query_db(f"SELECT * FROM game_prices WHERE id = \"{game_id}\"")[0]
    image_link_dict = query_db(f"SELECT image_link FROM game_images WHERE id = \"{game_id}\"")[0]
    shop_links = query_db( f"SELECT zaka_zaka_link, steam_pay_link, gabe_store_link FROM game_links WHERE id = \"{game_id}\"")[ 0]
    game_title = query_db(f"SELECT name FROM game_names WHERE id = \"{game_id}\"")[0]
    game.update(game_title)
    game.update(image_link_dict)
    game.update(shop_links)
    return jsonify(game)

if __name__ == '__main__':
    app.run(debug=True)

