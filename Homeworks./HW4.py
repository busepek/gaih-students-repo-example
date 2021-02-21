import sys
import random
import time

class Hangman:
    def __init__(self):
        self.screen = []
        self.attempts = 6
        self.words = ["turkey", "hungary", "america", "germany", "spain", "azerbaijan", "netherlands", "japan", "portugal", "malaysia", "sweden"]
        self.random_word = ""

    def main(self):
        name = input("Please write your name: ")
        print("Welcome {}! Ready for the game?".format(name))
        while True:
            start = input("Write YES or NO: ").lower()
            if start == "yes":
                self.random_word = random.choice(self.words).lower()
                print("Your game is starting! Please wait...")
                for i in range(30):
                    time.sleep(0.1)
                    print(".", end = " ")
                print(" ", "You have {} attempts! Good luck!".format(self.attempts), sep = "\n")
                print("The word has", len(self.random_word), "letters in it!")
                self.set_up()
                self.play()
                break
            elif start == "no":
                sys.exit("Good bye! :)")
            else:
                print("Please write YES or NO !!!", "Try again: ", sep = "\n")
                continue
    def set_up(self):
        for i in range(len(self.random_word)):
            self.screen.append("_")
    def play(self):
        guessed_letters = []
        while self.attempts > 0:
            letter = input("Guess a letter: ").lower()
            if letter in self.random_word and letter not in guessed_letters:
                guessed_letters.append(letter)
                self.screen_change(letter)
                print(self.screen)
                self.win_check()
            elif letter in guessed_letters:
                print("You have already guessed this letter! Try again!", self.screen, "Guess a letter: ", sep = "\n")
            else:
                guessed_letters.append(letter)
                print("That letter does not exist in the word :( Try again!")
                self.attempts -= 1
                print("You have {} attempts left.".format(self.attempts), self.screen, "Try again: ", sep = "\n")
            print(self.screen)
        print("You are out of lives! The word was " + self.random_word)

    def screen_change(self,letter):
        for i, lt in enumerate(self.random_word):
            if letter == lt:
                self.screen[i] = letter
    def win_check(self):
        if self.screen == list(self.random_word):
            print("Congrats! You won!! :)")
            sys.exit()

new_game = Hangman()
new_game.main()