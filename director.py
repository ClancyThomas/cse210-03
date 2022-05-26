from parachute import Image
from guessHandler import guessHandler
from wordHandler import wordHandler

class director:

    def __init__(self):
        self.lives = 5
        self.parachute = Image()
        self.guessHandler = guessHandler()
        self.wordHandler = wordHandler()

    def startGame(self):
        print("### Welcome to the Jumper Game ###")
