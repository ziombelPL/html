from flask import Flask
from random import randint

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Witaj świecie!</h1><a href='/druga'>Przejdź do drugiej strony</a>"

@app.route("/druga")
def druga():
    return f"<p>Jakaś podstrona. Losowa liczba: {randint (1, 100)}</p><a href='/'>Przejdź do strony głównej</a>"

app.run(debug=True)