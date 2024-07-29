import random

# Harita oluşturma
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]


# Haritayı ekrana yazdırma
def print_map(map):
    for row in map:
        print(" ".join(row))


print("Original Map:")
print_map(map)

# Kullanıcıdan pozisyon alma
position = input("Where do you want to put the treasure? (Enter in format 'row,col'): ")

# Pozisyonu ayrıştırma ve kontrol etme
try:
    horizontal, vertical = map(int, position.split(","))

    if 1 <= horizontal <= 3 and 1 <= vertical <= 3:
        # Haritaya 'X' yerleştirme
        map[horizontal - 1][vertical - 1] = "X"

        # Güncellenmiş haritayı ekrana yazdırma
        print("Updated Map:")
        print_map(map)
    else:
        print("Position out of range. Please enter values between 1 and 3 for both row and column.")
except ValueError:
    print("Invalid input. Please enter the position in format 'row,col' with numeric values.")
except IndexError:
    print("An error occurred while updating the map.")
