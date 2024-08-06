from flask import Flask


def make_bold(function):
    def wrapper(*args, **kwargs):
        return "<b>" + function(*args, **kwargs) + "</b>"

    return wrapper


def make_emphasis(function):
    def wrapper(*args, **kwargs):
        return "<em>" + function(*args, **kwargs) + "</em>"

    return wrapper


def make_underline(function):
    def wrapper(*args, **kwargs):
        return "<u>" + function(*args, **kwargs) + "</u>"

    return wrapper


app = Flask(__name__)


@app.route('/')
def home():
    return (
        "<h1>Hello World!</h1>"
        "<p>This is a paragraph.</p>"
        "<p>This is another paragraph.</p>"
    )


@app.route('/about')
def about():
    return (
        "<h1>About</h1>"
        "<p>This is a paragraph.</p>"
        "<p>This is another paragraph.</p>"
    )


@app.route('/contact')
def contact():
    return (
        "<h1>Contact</h1>"
        "<p>This is a paragraph.</p>"
        "<p>This is another paragraph.</p>"
    )


@app.route('/hello')
def hello_page():
    return (
        "<h1>Hello World!</h1>"
        "<p>This is a paragraph.</p>"
        "<p>This is another paragraph.</p>"
    )


@app.route('/hello/<name>')
@make_bold
@make_emphasis
@make_underline
def hello_name(name):
    return (
        f"<h1>Hello {name}!</h1>"
        "<p>This is a paragraph.</p>"
        "<p>This is another paragraph.</p>"
    )


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
