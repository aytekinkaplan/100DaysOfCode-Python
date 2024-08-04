sentence = input("Enter a sentence: ")


# 🚨 Don't change code above 👆

# Write your code below 👇
def word_lengths(sentence):
    # Split the sentence into a list of words
    words = sentence.split()

    # Use dictionary comprehension to create a dictionary with word lengths
    result = {word: len(word) for word in words}

    return result


# Calculate the result
result = word_lengths(sentence)

# Output the result
print(result)
