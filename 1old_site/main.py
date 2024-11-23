from flask import Flask, render_template
from random import randint

app = Flask(__name__)

@app.route("/")
def hello():
    losowa = randint(1, 100)
    return render_template("index.html", liczba=losowa)

@app.route("/druga")
def druga():
    return f"<p>Jakaś podstrona. Losowa liczba: {randint (1, 100)}</p><a href='/'>Przejdź do strony głównej</a>"

@app.route("/<zmienna>")
def testowa(zmienna):
    if zmienna == "test1":
        return "Napis 1"
    elif zmienna == "test2":
        return "Napis2"
    else:
        return f"Nie ma takiej podstrony jak {zmienna}"

@app.route("/<test>/<inna>")
def testowa2(test, inna):
    return f"Wartość zmiennej 1 to {test}, natomiast w zmiennej 2 to {inna}"



app.run(debug=True)