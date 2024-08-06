# save this as app.py
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return (
        "<h1>Hello World!</h1>"
        "<p>This is a paragraph.</p>"
        "<p>This is another paragraph.</p>"
    )
