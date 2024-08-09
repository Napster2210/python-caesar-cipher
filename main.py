import art


def caesar_cipher(text, shift, mode):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    shift = shift % len(alphabet)  # Handle shifts larger than the alphabet length
    if mode == "decode":
        shift = -shift

    result = [
        alphabet[(alphabet.index(letter) + shift) % len(alphabet)] if letter in alphabet else letter
        for letter in text.lower()
    ]
    return ''.join(result)


def main():
    print(art.logo)

    while True:
        mode = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n")
        shift = int(input("Type the shift number:\n"))

        result = caesar_cipher(text, shift, mode)
        print(f"Here is the {mode}d result: {result}")

        if input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower() != 'yes':
            print("Goodbye")
            break


if __name__ == "__main__":
    main()
