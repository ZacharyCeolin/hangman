# Hangman Game (`hangman.py`)

A simple **command-line Hangman game** in Python where one player sets a secret word, and another player tries to guess it one letter at a time.

## Features

- Secret word input is hidden (using `getpass`) so the guessing player cannot see it.
- Input validation ensures that only letters are accepted for both the secret word and guesses.
- Tracks guessed letters and prevents duplicate guesses.
- Displays the current state of the word with underscores for unguessed letters.
- Shows a visual representation of the hangman as lives decrease.
- Ends the game when the player either guesses the word correctly or runs out of lives.

## How to Play

1. Run the script in your terminal:

   ```bash
   python hangman.py 

2. Enter the secret word when prompted (input will be hidden).

3. The guessing player enters letters one at a time.

4. The game displays:

- Correct guesses in the word.

- Guessed letters.

- Remaining lives.

- The hangman ASCII art for visual feedback.

5. The game ends when:

- The player guesses all letters correctly (win), or

- The player runs out of lives (loss).

## Rules

- Only alphabetic characters are allowed.

- Guess one letter at a time.

- Repeated guesses are not allowed.

- The player has 6 lives before the hangman is complete.

## Example Output

```
_ _ _ _ _ 
Guess a Letter: a
There is no A in the secret word
Lives remaining : 5
*********
 
     O    
    /|\     
    /     
 
*********
```

## Requirements

- Python 3.x

*No external libraries are required; the script uses only built-in Python modules (getpass and re).*
