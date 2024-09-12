import random

def main():

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
        welcome = "welcome to Hangman! You know the instructions"

        print(welcome)
        play_again = True
        
        while play_again:
               
                        words = ["hangman", "chairs", "backpack", "bodywash", "clothing",
                 "computer", "python", "program", "glasses", "sweatshirt",
                 "sweatpants", "mattress", "friends", "clocks", "biology",
                 "algebra", "suitcase", "knives", "ninjas", "shampoo"]
        
        chosen_word = random.choice(words).lower()
        
        player_guess = None

        guessed_letters = []
        words_guessed = []

        for letter in chosen_word:
                words_guessed.append("-")     

        joined_word = None

        print(HANGMAN[0])

        play_again = False

        attempts = len(len(HANGMAN) - 1)

        while attempts > 0 and "_" in words_guessed:
                print("You have {} attempts remaining ")
                joined_word = "".join(words_guessed)
                print (joined_word)

                try:
                        player_guess = str(input("Please select a letter between A-Z ")).lower()
                except:
                         print("This is invalid. Please try again.")

                         continue
                else:
                        if not player_guess.isalpha():
                                print("That is not a letter. Please try again.")
                                continue
                        elif len(player_guess ) > 1:
                                print("That is more than one letter. Please try again.")
                                continue
                        elif player_guess in guessed_letters:
                                print("You have already guessed that letter. Please try again")
                                continue
                        else:
                                pass
                guessed_letters.append(player_guess)
                for letter in range(len(chosen_word)):
                        if player_guess == chosen_word[letter]:
                                words_guessed[letter] = player_guess
                
                if player_guess not in chosen_word:
                        attempts -= 1
                        print(HANGMAN[len(HANGMAN)] - 1 - attempts)
        if "-" not in words_guessed:
                print(f"congratulations! {chosen_word} was the word")
        else:
                print(f"Unlucky! The word was {chosen_word}")

        print("Would you like to play again")
        
        response = input("> ").lower()
        if response not in ("yes", "y"):
            play_again = False

                


if __name__ == "__main__":
    main()
