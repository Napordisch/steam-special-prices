from flask import Flask, render_template, jsonify
from db import query_db

app = Flask(__name__)

@app.route('/')
def show_all_games_page():
    return render_template("games_page.html")

@app.route('/all-games-prices')
def get_games_prices():
    games_with_prices_and_images = query_db("SELECT * FROM game_prices")
    for game in games_with_prices_and_images:
        image_link_dict = query_db(f"SELECT image_link FROM game_images WHERE id = \"{game['id']}\"")[0]
        print(image_link_dict)
        game.update(image_link_dict)
    return jsonify(games_with_prices_and_images)

@app.route('/game-info')
def get_game_with_prices():
    pass



if __name__ == '__main__':
    app.run()

