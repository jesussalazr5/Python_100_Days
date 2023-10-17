import random
from Hangman_Art import stages, logo
from Hangman_Word import word_list
from replit import clear


chosen_word = random.choice(word_list)
number_letter = len(chosen_word)
print(f"{logo}")

display = []

for letter in chosen_word:
    display.append("_")

end_of_game = False
lives = 6
while end_of_game == False:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've ready already guessed {guess}")
    clear()

    for letter in range(len(chosen_word)):
        if chosen_word[letter] == guess:
            display[letter] = guess

    if guess not in chosen_word:
        print(f"You guessed {guess}, that´s not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lose")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print(f"You win.")

    print(stages[lives])
