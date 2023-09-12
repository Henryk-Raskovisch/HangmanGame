import os
import random
from hangman_words import word_list
from hangman_art import stages, logo

chosen_word = random.choice(word_list)
word_lenght = len(chosen_word)
lives = 6

print(logo)

#create blanks
display = []
for _ in range(word_lenght):
    display += "_"

print(f"{' '.join(display)}")

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: \n").lower()
    os.system("cls")

    if guess in display:
        print(f"You've already guessed the letter {guess}. Try again")

#check guessed letter
    for position in range(word_lenght):
        letter = chosen_word[position] 
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
       print(f"The letter '{guess}' is not in the word. You lose a life!")
        
    if guess not in chosen_word:
        lives -= 1 
    if lives == 0:
        end_of_game = True
        print("you've lost all your lives. You lose")
        print(f"The correct word is {chosen_word}")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You won")
    
    print(stages[lives])
 