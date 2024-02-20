MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ' ': ' '
}

def text_to_morse(text):
    return ' '.join([MORSE_CODE_DICT.get(char.upper(), char) for char in text])

def morse_to_text(morse_code):
    morse_code_dict_reverse = {v: k for k, v in MORSE_CODE_DICT.items()}
    return ''.join([morse_code_dict_reverse.get(code, ' ') for code in morse_code.split(' ')])

def main():
    print("Text to Morse Code Converter")

    while True:
        print("\n1. Convert text to Morse code\n2. Convert Morse code to text\n3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            input_text = input("Enter the text to convert to Morse code: ")
            morse_code = text_to_morse(input_text)
            print(f"Morse Code: {morse_code}")

        elif choice == '2':
            morse_code_input = input("Enter the Morse code to convert to text: ")
            decoded_text = morse_to_text(morse_code_input)
            print(f"Decoded Text: {decoded_text}")

        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
