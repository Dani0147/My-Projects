
#Our hangman game
import random

WORDLIST_FILENAME = 'C:\\game\\words.txt'

class HangmanGame:
    def __init__(self):

        self.words = self.loadWords()
        self.hangman_stages = [

            """
              ------------
              |          |
              |       (´･ω･`) <- Happy waiter ready to take your order.
              |          |  
              |         /|\\
              |        / | \\
              |          |
              |         / \\
              |        /   \\
              |        
             ---
            """,
            """
              ------------
              |          |
              |        (^_^) <- Still hopeful waiter.
              |          |  
              |         /|\\
              |        / | 
              |          |
              |         / 
              |        /   
              |        
             ---
            """,
            """
              ------------
              |          |
              |        (o_o) <- Slightly concerned waiter.
              |          |  
              |         /|\\
              |          | 
              |          |
              |          
              |          
              |        
             ---(^_^) <- Still hopeful waiter.
            """,
            """
              ------------
              |          |
              |        (ಠಿ_ಠ) <- Waiter starting to get angry.
              |          |  
              |         /|
              |          | 
              |          |
              |          
              |          
              |        
             ---
            """,
            """
              ------------
              |          |
              |        (ಠ_ಠ) <- Extremely displeased waiter.
              |          |  
              |          |
              |          | 
              |          |
              |          
              |          
              |        
             ---
            """,
            """
              ------------
              |          |
              |        (ಠ_ಠ) <- Extremely displeased waiter.
              |          
              |          
              |           
              |          
              |          
              |          
              |        
             ---
            """,
            """
              ------------
              |          |
              |        (x_x) <- The waiter is 'dead' from disappointment.
              |          
              |          
              |           
              |          
              |          
              |          
              |        
             ---
            """
        
        ]
    
    def loadWords(self):
        print("Loading word list from file...")
        with open(WORDLIST_FILENAME) as inFile:
            wordlist = inFile.read().split()
            print(len(wordlist), "words loaded.")
            return wordlist
    
    def play(self):
        word = random.choice(self.words)
        guessed_letters = []
        wrong_guesses = 0
        attempts = 6
        hint_shown = False

        while attempts > 0:
            print("\033[94m\nAttempts left:\033[0m", attempts)
            
            hidden_word = self.get_hidden_word(word, guessed_letters)
            print(hidden_word)
            
            english_guessed_letters = [letter for letter in guessed_letters if 'a' <= letter <= 'z']
            print("\033[91mGuessed letters:\033[0m ", ' '.join(english_guessed_letters))
            
            stage_index = min(wrong_guesses, len(self.hangman_stages) - 1)
            print("\033[95m" + self.hangman_stages[stage_index] + "\033[0m")

            if "_" not in hidden_word:
                print("\033[94mCongratulations!!! You guessed the word:\033[0m", word)
                break

            if wrong_guesses == 3 and not hint_shown:
                hint_letters = [l for l in word if l not in guessed_letters][:2]
                print(f"\033[93mHint: Here are 2 letters that are in the word:\033[0m {' '.join(hint_letters)}")
                hint_shown = True

            guess = input("\033[92mGuess a letter:\033[0m ").lower()

            if not guess.isalpha() or len(guess) != 1 or not 'a' <= guess <= 'z':
                print("\033[91mPlease enter only one English alphabet letter.\033[0m")
                continue

            if guess in guessed_letters:
                print("\033[91mYou have already guessed that letter.\033[0m")
                continue

            guessed_letters.append(guess)

            if guess in word:
                print("\033[92mCorrect guess!\033[0m")
            else:
                print("\033[91mWrong guess!\033[0m")
                wrong_guesses += 1
                attempts -= 1

                if attempts == 0:
                    print("\033[95m" + self.hangman_stages[-1] + "\033[0m") 
                    print("\033[91mSorry, you're dead. The word was:\033[0m", word)

    def get_hidden_word(self, word, guessed_letters):
        return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def main():
    print("\033[92mHello! Welcome to our hangman restaurant game. We hope you will enjoy it! 😊\033[0m")
    game = HangmanGame()
    while True:
        print("\n\033[95mMain Menu:\033[0m")
        print("\033[94m1. Play Hangman\033[0m")
        print("\033[94m2. Exit\033[0m")
        choice = input("\033[93mEnter your choice (1 or 2):\033[0m ")
        
        if choice == "1":
            print("\033[96mStarting the game... Good luck!\033[0m")
            input('\033[93mPress Enter to continue...\033[0m')
            print("\033c", end="")
            game.play()
        
        elif choice == "2":
            print("\033[91mThanks for playing! Goodbye.\033[0m")
            break

        else:
            print("\033[91mInvalid choice, please enter 1 or 2.\033[0m")
            input('\033[93mPress Enter to continue...\033[0m')
            print("\033c", end="")

main()



 



