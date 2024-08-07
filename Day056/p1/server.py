from flask import Flask, render_template
import random
import datetime

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    random_number1 = random.randint(1, 10)
    multiplier = random_number * random_number1
    current_year = datetime.datetime.now().year
    return render_template("index.html", multiplier=multiplier, num=random_number, year=current_year)


if __name__ == "__main__":
    app.run(debug=True)
