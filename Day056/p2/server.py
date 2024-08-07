from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    return render_template("index.html", num=random_number, year=current_year)


@app.route("/guess/<name>")
def guess(name):
    gender_url = f"https://api.genderize.io/?name={name}"
    gender_response = requests.get(gender_url)
    requests_data = gender_response.json()
    gender = requests_data["gender"]

    age_url = f"https://api.agify.io/?name={name}"
    age_response = requests.get(age_url)
    requests_data = age_response.json()
    age = requests_data["age"]
    return render_template("guess.html", person_name=name, gender=gender, age=age)


@app.route("/blog/<int:num>")
def get_blog(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts, num=num)


if __name__ == "__main__":
    app.run(debug=True)
