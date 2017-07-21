import getpass

class Hangman:
    """Simple Hangman game"""
    def __init__(self):
        """Prepare some global vars."""
        self.lives = 4
        self.guessed_chars = []
        self.done = False
        self.placehoder = "_"

    def start(self):
        """Initiate the game."""
        print("\nWELCOME TO HANGMAN!\n")
        self.word = getpass.getpass('Pick a word to guess:')
        self.guess = [self.placehoder] * len(self.word)

        print("\nLet the game begin!")
        print("Word to guess:" + "".join(self.guess))

        # Iterate the game.
        while not self.done:
            print("\n")
            self.print_iteration()
            self.guess_iteration()

        # End the game with message.
        print(self.get_ending_game_string())

    def print_iteration(self):
        """Print current iteration."""
        print("Remaining lives: " + str(self.lives))
        print("Guessed letters: " + ", ".join(self.guessed_chars))
        print("So far correctly guessed:" + "".join(self.guess))

    def guess_iteration(self):
        """Guessing iteration."""

        # Get users guess.
        user_guess = input("Pick a letter:")

        # Do not allow repeated guesses.
        if user_guess in self.guessed_chars:
            print("You already tried this one! Try again...")
        else:
            self.guessed_chars.append(user_guess)

            # Users guess is in guessed word.
            if user_guess in self.word:
                print("You got another one!")

                # Change appropriate placeholders to guessed letter.
                for i, c in enumerate(self.word):
                    if user_guess == c:
                        self.guess[i] = c

                # End the game if we got all the placeholders replaced.
                if self.placehoder not in self.guess:
                    self.done = True
            else:
                # Incorrect guess, subtract live
                print("Nope...that just cost you one life!")
                self.lives -= 1
                # End the game if there are no lives.
                if self.lives <= 0:
                    self.done = True

    def get_ending_game_string(self):
        """Get ending game string"""
        if self.lives <= 0:
            return "Sorry, you are out of lives!...\nThe word you were trying to guess was \"" + self.word + "\"."
        else:
            return "YEAH! You got it!"

if __name__ == '__main__':
    hangman = Hangman()
    hangman.start()
