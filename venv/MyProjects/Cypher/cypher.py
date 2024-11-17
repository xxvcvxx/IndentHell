alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input('Please enter "d" for decryption or "e" for encryption: ')
while direction != 'e' and direction != 'd':
    print("Invalid input. Please enter only one character (e.g., 'd' or 'e').")
    direction = input('Please enter "d" for decryption or "e" for encryption: ')
text = input('Please enter the text to be processed: ')

shift = input('Please enter the shift number (an integer): ')
while not shift.isdigit():
    print("Invalid input. Please enter a valid integer.")
    shift = input('Please enter the shift number (an integer): ')


def encrypt(original_text, shift_amount):
    encrypted_text = ''

    for char in original_text:
        if char in alphabet:
            i = alphabet.index(char)
            encrypted_text += alphabet[(i + int(shift_amount)) % len(alphabet)]
        else:
            encrypted_text += char

    print(encrypted_text)


def decrypt(original_text, shift_amount):
    decrypted_text = ''
    for char in original_text:
        if char in alphabet:
            i = alphabet.index(char)
            decrypted_text += alphabet[(i - int(shift_amount)) % len(alphabet)]
        else:
            decrypted_text += char

    print(decrypted_text)


if direction == 'e':
    encrypt(text, shift)
elif direction == 'd':
    decrypt(text, shift)
