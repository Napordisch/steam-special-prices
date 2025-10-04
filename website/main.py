from flask import Flask, jsonify, send_from_directory
from flask_cors import cross_origin

from db import query_db

app = Flask(__name__, static_folder='static')


@app.route('/static/<path:filename>')
def send_static(filename):
    return send_from_directory('static', filename)


@app.route('/<game_id>')
def show_game_comparision_page(game_id):
    return send_from_directory('static', "price-comparison-page.html")


@app.route('/')
def show_all_games_page():
    return send_from_directory('static', "main_page.html")

@app.route('/all-games-prices')
@cross_origin(origin="http://localhost:3000")
def get_games_prices():
    games_with_prices_and_images = query_db("""
       SELECT
            game_prices.*,
            game_images.image_link,
            game_links.zaka_zaka_link,
            game_links.steam_pay_link,
            game_links.gabe_store_link,
            game_names.name
        FROM game_prices
        LEFT JOIN game_images  ON game_prices.id = game_images.id
        LEFT JOIN game_links   ON game_prices.id = game_links.id
        LEFT JOIN game_names   ON game_prices.id = game_names.id
        ORDER BY game_prices.place_in_top ASC
    """)

    return jsonify(games_with_prices_and_images)

@app.route('/game-info/<game_id>')
@cross_origin(origin="http://localhost:3000")
def get_game_with_prices(game_id):
    sql = """
        SELECT
            game_prices.*,
            game_images.image_link,
            game_links.zaka_zaka_link,
            game_links.steam_pay_link,
            game_links.gabe_store_link,
            game_names.name
        FROM game_prices
        LEFT JOIN game_images  ON game_prices.id = game_images.id
        LEFT JOIN game_links   ON game_prices.id = game_links.id
        LEFT JOIN game_names   ON game_prices.id = game_names.id
        WHERE game_prices.id = %s
    """
    rows = query_db(sql, (game_id,))
    if not rows:
        abort(404, "Game not found")
    game = dict(rows[0])
    return jsonify(game)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
