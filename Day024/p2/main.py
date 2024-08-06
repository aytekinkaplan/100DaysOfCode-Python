# Dosyayı ekleme modunda aç ve yaz
with open("my_file.txt", mode="a") as file:
    file.write("\nI also love finding meaning in large datasets.")
    file.write("\nI love creating apps that can help people.")

# Dosyayı okuma modunda aç ve oku
with open("my_file.txt", mode="r") as file:
    contents = file.read()
    print(contents)
