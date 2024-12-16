from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def show_all_games():
    return render_template("games_page.html")

if __name__ == '__main__':
    app.run(debug=True)