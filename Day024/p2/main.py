# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

with open("my_file.txt", mode="a") as file:
    file.write("\nI also love finding meaning in large datasets.")
    file.write("\nI love creating apps that can help people.")
    print(file.read())
