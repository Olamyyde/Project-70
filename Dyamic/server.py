from ast import Num
from flask import Flask, render_template
from random import randint

app = Flask(__name__)


@app.route('/')
def home():
    rando = randint(2,5)
    return render_template("index.html", Num=rando)



if __name__ == "__main__":
    app.run(debug=True)