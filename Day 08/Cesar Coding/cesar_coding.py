from alphabet import alphabet
from symbols import symbols
from replit import clear
from art import logo


end_of_game = False
# print(logo)


def play_game():
    command = False
    while command == False:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        if direction == "encode" or direction == "decode":
            text = input("\nType your message:\n").lower()
            shift = int(input("\nType the shift number:\n"))
            if shift > len(alphabet):
                shift = shift % len(alphabet)
            command = True
        else:
            print(f" {' - '*10} Erro command '{direction}' not found {' - '*10}\n")
    return text, shift, direction


def cesar(plain_text, amount_shift, direction):
    global end_of_game
    cipher_text = ""
    for letter in plain_text:
        if letter in symbols:
            cipher_text += letter
        elif letter not in symbols:
            symbols.append(letter)
            cipher_text += letter
        else:
            position = alphabet.index(letter)
            if direction == "encode":
                new_position = position + amount_shift
                if new_position >= len(alphabet):
                    new_letter = alphabet[position - len(alphabet) + amount_shift]
                    cipher_text += new_letter
                else:
                    new_letter = alphabet[new_position]
                    cipher_text += new_letter
            else:
                new_position = position - amount_shift
                if new_position >= len(alphabet):
                    new_letter = alphabet[position - len(alphabet) - amount_shift]
                    cipher_text += new_letter
                else:
                    new_letter = alphabet[new_position]
                    cipher_text += new_letter
    print(f"The {direction} text is: - -> {cipher_text} <- - -")
    continue_game = input(f"You want continue decoding? - - yes or not --\n").lower()
    if continue_game != "y":
        end_of_game = True
    return end_of_game


while end_of_game == False:
    text, shift, direction = play_game()
    end_of_game = cesar(plain_text=text, amount_shift=shift, direction=direction)
print(f"Goodbye")
