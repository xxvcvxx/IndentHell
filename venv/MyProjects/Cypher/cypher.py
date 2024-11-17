alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input('bla')
text = input('text')
shift = input('liczba')


def encrypt(original_text, shift_amount):
    encrypted_text = ''

    for char in original_text:
        if char in alphabet:
            i = alphabet.index(char)
            encrypted_text += alphabet[(i + int(shift_amount)) % len(alphabet)]

    print(encrypted_text)


encrypt(text, shift)
