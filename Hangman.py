import getpass
import re

secret_input = getpass.getpass("Enter the secret word: ")
secret_word = ""
validator = 0
game = 0
lives = 6
guessed_letters = []
hidden_word = []


while validator == 0:
    if re.search(r"[^A-Za-z]", secret_input):
        print("Your word can only have letter!")
    else:
        print("Word Accepted!")
        secret_word = secret_input.lower()
        validator += 1


for i in range(len(secret_word)):
    hidden_word.append("_")
    hidden_word.append(" ")
print("".join(hidden_word))
    

while game == 0:
    validator = 0
    while validator == 0:
        guess_input = input("Guess a Letter:")

        if re.search(r"[^A-Za-z]", guess_input):
            print("You can only guess letters!")
        else:
            if len(guess_input) > 1:
                print("You can only guess one letter at a time!") 
            elif len(guess_input) == 0:
                print("You have to guess a letter!") 
            else: 
                if guess_input.lower()in guessed_letters:
                    print(f"{guess_input} has already been guessed.")
                else:
                    guess = guess_input.lower()
                    guessed_letters.append(guess)
                    print(guessed_letters)
                    validator += 1
    
                    for i in range(len(secret_word)):
                        if secret_word[i] == guess:
                            hidden_word[i*2] = guess
                    if guess in secret_word:
                        print(f"There is a {guess.upper()} in the secret word")
                    else:
                        print(f"There is no {guess.upper()} in the secret word")
                        lives -= 1
                    print("".join(hidden_word))



