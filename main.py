# Hangman game challenge
# 100 Days of Code (Python) course

import random
from replit import clear

from hangman_words import word_list
chosen_word = random.choice(word_list)

word_length = len(chosen_word)

end_of_game = False
lives = 6

from hangman_art import stages, logo
print(logo)

#Testing code
print(f'Hint: the solution is {chosen_word}.')

#Create blanks
display = []
for i in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()

    if guess in display:
        print(f"You've already guessed {guess}") 

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        
        if letter == guess:
            display[position] = letter                     

    #Check if user is wrong.
    if guess not in chosen_word:
        print(f"You guess {guess}. That's not in the word. You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])