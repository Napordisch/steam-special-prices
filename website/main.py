from flask import Flask, jsonify, send_from_directory, render_template
from flask_cors import cross_origin
from game import Game

from db import query_db

app = Flask(__name__, static_folder='static')

VUE_FRONTEND_ORIGIN="http://localhost:5173"


@app.route('/static/<path:filename>')
def send_static(filename):
    return send_from_directory('static', filename)

@app.route('/favicon.ico')
def favicon():
    return '', 204


@app.route('/')
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


    return render_template('main_page.html.jinja', game_cards=map(Game, games_with_prices_and_images))

@app.route('/<game_id>')
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
    game = Game(dict(rows[0]))

    return render_template('price_comparison_page.html.jinja', game=game)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
