alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def encrypt(text, shift):
    # Shift değerini 26 ile sınırlıyoruz
    shift = shift % 26
    cipher_text = ""

    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift) % 26
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        else:
            # Eğer harf değilse olduğu gibi ekliyoruz
            cipher_text += letter

    print(f"The encoded text is {cipher_text}")


text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

encrypt(text=text, shift=shift)
