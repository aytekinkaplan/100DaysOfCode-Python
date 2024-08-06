import random
from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML templates
template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Guess the Number</title>
</head>
<body>
    <h1>Guess the Number Game</h1>
    <p>{{ message }}</p>
    <form method="post">
        <label for="guess">Enter your guess (1-10): </label>
        <input type="number" id="guess" name="guess" min="1" max="10" required>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
"""

# Store the secret number in a global variable
SECRET_NUMBER = random.randint(1, 10)


@app.route("/", methods=["GET", "POST"])
def guess_number():
    global SECRET_NUMBER
    message = "Guess a number between 1 and 10"
    if request.method == "POST":
        guess = int(request.form["guess"])
        if guess == SECRET_NUMBER:
            message = "Correct! You guessed the number!"
            SECRET_NUMBER = random.randint(1, 10)  # Reset the game with a new number
        elif guess < SECRET_NUMBER:
            message = "Too low! Try again."
        else:
            message = "Too high! Try again."
    return render_template_string(template, message=message)


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
