def write_to_file(file_path, lines):
    """
    Dosyaya satırları yazar.

    :param file_path: Yazılacak dosyanın yolu
    :param lines: Dosyaya yazılacak satırların listesi
    """
    with open(file_path, mode="w") as file:
        for line in lines:
            file.write(line + "\n")


def read_from_file(file_path):
    """
    Dosyadan içeriği okur ve döndürür.

    :param file_path: Okunacak dosyanın yolu
    :return: Dosyanın içeriği
    """
    with open(file_path, mode="r") as file:
        return file.read()


# Dosyaya yazılacak satırlar
lines_to_write = [
    "I love creating new files!",
    "",
    "I enjoy learning new programming languages.",
    "Reading books is one of my favorite pastimes.",
    "I find joy in solving complex problems.",
    "I love creating new files!",
    "Cooking and trying new recipes is fun.",
    "I love creating new files!",
    "Traveling to new places is exciting.",
    "Music and movies are great sources of inspiration.",
    "I love creating new files!",
    "Spending time with family and friends is precious."
]

# Dosya yolu
file_path = "my_file.txt"

# Dosyaya yaz
write_to_file(file_path, lines_to_write)

# Dosyadan oku ve içeriği yazdır
file_content = read_from_file(file_path)
print(file_content)
