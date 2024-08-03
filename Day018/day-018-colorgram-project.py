import colorgram
import turtle as t
import random
from PIL import Image, ImageDraw


def extract_colors(image_path, num_colors):
    colors = colorgram.extract(image_path, num_colors)
    rgb_colors = []
    for color in colors:
        r, g, b = color.rgb
        rgb_colors.append((r, g, b))
    return rgb_colors


def create_art(colors, dot_count, dot_size, canvas_size):
    image = Image.new("RGB", (canvas_size, canvas_size), "white")
    draw = ImageDraw.Draw(image)

    for y in range(dot_count):
        for x in range(dot_count):
            color = random.choice(colors)
            x_pos = x * dot_size + dot_size // 2
            y_pos = y * dot_size + dot_size // 2
            draw.ellipse([x_pos - dot_size // 2, y_pos - dot_size // 2,
                          x_pos + dot_size // 2, y_pos + dot_size // 2],
                         fill=color)

    return image


# Ana program
num_colors = 10
dot_count = 20
dot_size = 40
canvas_size = dot_count * dot_size

# Renkler çıkarılıyor
colors = extract_colors(r"C:\Users\aonik\PycharmProjects\100DaysOfCode-Python\Day018\example.jpeg", num_colors)

# Sanat eseri oluşturuluyor
art_image = create_art(colors, dot_count, dot_size, canvas_size)

# JPEG olarak kaydetme
output_path = r"C:\Users\aonik\PycharmProjects\100DaysOfCode-Python\Day018\output_art.jpeg"
art_image.save(output_path, "JPEG")

print(f"Sanat eseri {output_path} konumuna JPEG olarak kaydedildi.")

# Görüntüyü ekranda gösterme (isteğe bağlı)
art_image.show()
