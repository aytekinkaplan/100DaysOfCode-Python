# Love Calculator

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_names = (name1 + name2).lower()

t = combined_names.count("t")
r = combined_names.count("r")
u = combined_names.count("u")
e = combined_names.count("e")

l = combined_names.count("l")
o = combined_names.count("o")
v = combined_names.count("v")
e = combined_names.count("e")

love_score = (t + r + u + e) * 10 + (l + o + v + e)

print(f"Your score is {love_score}, you go together like coke and mentos.")