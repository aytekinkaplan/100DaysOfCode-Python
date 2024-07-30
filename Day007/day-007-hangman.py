import random

# List of possible words for the game
word_list = ["python", "java", "hangman", "development", "programming"]

# Randomly select a word from the list
word = random.choice(word_list)
word_length = len(word)
hidden_word = ['_'] * word_length

# Track the number of errors and guessed letters
errors = 0
max_errors = 6
guessed_letters = []


def display_hidden_word(hidden_word):
    """
    This function joins the elements of the hidden_word list into a string
    separated by spaces and returns the resulting string.
    """
    return " ".join(hidden_word)


def draw_hangman(errors):
    """
    This function draws the hangman figure based on the number of errors.
    """
    hangman_pics = [
        """
           ------
           |    |
                |
                |
                |
                |
        --------
        """,
        """
           ------
           |    |
           O    |
                |
                |
                |
        --------
        """,
        """
           ------
           |    |
           O    |
           |    |
                |
                |
        --------
        """,
        """
           ------
           |    |
           O    |
          /|    |
                |
                |
        --------
        """,
        """
           ------
           |    |
           O    |
          /|\\   |
                |
                |
        --------
        """,
        """
           ------
           |    |
           O    |
          /|\\   |
          /     |
                |
        --------
        """,
        """
           ------
           |    |
           O    |
          /|\\   |
          / \\   |
                |
        --------
        """
    ]
    print(hangman_pics[errors])


# Main game loop
while errors < max_errors and '_' in hidden_word:
    print(f"\nHidden word: {display_hidden_word(hidden_word)}")
    print(f"Guessed letters: {', '.join(guessed_letters)}")
    print(f"Number of incorrect guesses: {errors}")
    draw_hangman(errors)

    # Get a letter guess from the user
    guess = input("Guess a letter: ").lower()

    # Check if the letter has already been guessed
    if guess in guessed_letters:
        print("You have already guessed that letter. Try a different letter.")
        continue

    # Add the guessed letter to the list of guessed letters
    guessed_letters.append(guess)

    # Check if the guessed letter is in the word
    if guess in word:
        # If the letter is in the word, reveal its positions in the hidden word
        for i in range(word_length):
            if word[i] == guess:
                hidden_word[i] = guess
    else:
        # If the letter is not in the word, increase the error count
        errors += 1
        print("Incorrect guess!")

# Check if the game was won or lost
if '_' not in hidden_word:
    print(f"Congratulations! You guessed the word correctly: {word}")
else:
    draw_hangman(errors)
    print(f"You lost! The correct word was: {word}")
