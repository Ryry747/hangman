import random
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
word_list = ('apple pear grape kiwi orange').split()

class Hangman:
    word = None
    lives = None
    correct_guesses = None

    def __init__(self, lives, word_list) -> None:
        self.lives = lives
        self.word = word_list[random.randint(0, len(word_list)-1)].lower()
        self.correct_guesses = []

    def get_user_input(self):
        Guess = ""
        while not(Guess.isalpha() and len(Guess) == 1):
            Guess = input("Enter a single letter: ").lower()

        return Guess

    def check_guess(self, Guess):
        if(Guess in self.word):

            if(Guess in self.correct_guesses):
                print("You have already guessed {}".format(Guess))
            else:
                print("Good guess. {} was in the word!".format(Guess))
                self.correct_guesses.append(Guess)

        else:
            print("Sorry {} is not in the word. Try again".format(Guess))
            return False
        
        return True

    def display_guessed_letters(self):
        output = ""
        for letter in self.word:
            if(letter not in self.correct_guesses):
                letter = "_"
            output += letter

        print(HANGMANPICS[-self.lives])
        print(output + "\n")

    def play_game(self):
        print("The word is {length} letters long".format(length = len(self.word)))
        word_guessed = False

        #Main Gameplay Loop
        while(self.lives > 0 and not word_guessed):

            self.display_guessed_letters()

            Guess = self.get_user_input()
            if(not self.check_guess(Guess)): self.lives -= 1

            word_guessed = (len(self.correct_guesses) == len(set(self.word)))

        #Win/Loss Message
        if (word_guessed):
            print("\nCongratulations you guessed the word. The word was {}".format(self.word))
        else:
            print("\nYou ran out of lives, the word was {}".format(self.word))


def main():
    while(True):
        hangman = Hangman(7, word_list)
        hangman.play_game()
        user_quit = input("Type q to quit. Type anything else to play again: ").lower()
        if(user_quit == "q"): break

main()
#%%
