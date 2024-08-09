languages = ["Python", "C#", "Java", "Javascript", "React"]

result = languages
result = type(languages)
result = languages[0:2]
result = languages[2:]
result = languages[:3]
result = languages[-1]
result = languages[-4:-1]
# languages[0] = "Html"
languages[-1] = "Html"
result = len(languages)
result = languages + ["Angular", "Vuejs"]

# if block => Conditional statements
if "Python" in languages:
    print("The value is an element of the list")

# loops
for x in languages:
    print(x)

del languages[0]

result = languages

print(result)
