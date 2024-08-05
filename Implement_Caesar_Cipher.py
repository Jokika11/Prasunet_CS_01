def encrypt(plain_text, shift_amount):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cipher_text = ""
    for letter in plain_text:
        if letter.isalpha():
            position = alphabet.index(letter.lower())
            new_position = (position + shift_amount) % 26
            new_letter = alphabet[new_position]
            if letter.isupper():
                new_letter = new_letter.upper()
            cipher_text += new_letter
        else:
            cipher_text += letter
    return cipher_text


def decrypt(cipher_text, shift_amount):
    return encrypt(cipher_text, -shift_amount)


def main():
    print('----------------------------------------')
    print("~Welcome to the Caesar Cipher Program!~")
    print('----------------------------------------')
    while True:
        print("\nOptions:")
        print("1. Encode a message")
        print("2. Decode a cipher")
        print("3. Exit")
        print('  ')
        choice = input("Choose an option (1/2/3): ")
        print('  ')
        if choice == '1':
            text = input("Enter your message: ").lower()
            shift = int(input("Enter the shift number: "))
            result = encrypt(text, shift)
            print('*************************************************')
            print(f"Encoded message: {result}")
            print('*************************************************')

        elif choice == '2':
            text = input("Enter the cipher text: ").lower()
            shift = int(input("Enter the shift number: "))
            result = decrypt(text, shift)
            print('*************************************************')
            print(f"Decoded message: {result}")
            print('*************************************************')


        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid input. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
