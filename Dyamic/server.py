from ast import Num
from flask import Flask, render_template
from random import randint
from datetime import datetime


app = Flask(__name__)


@app.route('/')
def home():
    rando = randint(2,5)
    current_year = datetime.now().year
    return render_template("index.html", Num=rando, year=current_year)



if __name__ == "__main__":
    app.run(debug=True)