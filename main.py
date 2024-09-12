import random




HANGMAN = (
"""
-----
|   |
|
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|  -+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  |
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | 
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | | 
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | | 
|  | | 
|
--------
""")
        
import random

def main():
    welcome = ['Welcome to Hangman! A word will be chosen at random and',
               'you must try to guess the word correctly letter by letter',
               'before you run out of attempts. Good luck!']

    for line in welcome:
        print(line)
    
    play_again = True  # Move play_again out of the for loop

    while play_again:
        words = ["hangman", "chairs", "backpack", "bodywash", "clothing",
                 "computer", "python", "program", "glasses", "sweatshirt",
                 "sweatpants", "mattress", "friends", "clocks", "biology",
                 "algebra", "suitcase", "knives", "ninjas", "shampoo"]

        chosen_word = random.choice(words).lower()
        guessed_letters = []
        word_guessed = ["-"] * len(chosen_word)

        print(HANGMAN[0])  # Assuming HANGMAN is already defined
        attempts = len(HANGMAN) - 1

        while attempts != 0 and "-" in word_guessed:
            print(f"\nYou have {attempts} attempts remaining")
            print("".join(word_guessed))

            player_guess = input("\nPlease select a letter between A-Z\n> ").lower()

            if not player_guess.isalpha() or len(player_guess) > 1 or player_guess in guessed_letters:
                print("Invalid guess. Please try again.")
                continue

            guessed_letters.append(player_guess)

            if player_guess in chosen_word:
                for i in range(len(chosen_word)):
                    if player_guess == chosen_word[i]:
                        word_guessed[i] = player_guess
            else:
                attempts -= 1
                print(HANGMAN[len(HANGMAN) - attempts - 1])

        if "-" not in word_guessed:
            print(f"\nCongratulations! {chosen_word} was the word.")
        else:
            print(f"\nUnlucky! The word was {chosen_word}.")

        print("\nWould you like to play again?")
        response = input("> ").lower()
        if response not in ("yes", "y"):
            play_again = False

if __name__ == "__main__":
    main()

