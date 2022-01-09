from flask import Flask
import random


random_no = random.randint(0,9)


app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Guess a number between 0 and 9</h1>"\
        "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


# @app.route("/entry/id")
# def guess():





if __name__ == "__main__":
    app.run(debug = True)