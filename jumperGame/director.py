from jumperGame.parachute import Image
from jumperGame.guessHandler import guessHandler
from jumperGame.wordHandler import wordHandler

class director:

    def __init__(self):
        self.lives = 5
        self.parachute = Image()
        self.guessHandler = guessHandler()
        self.wordHandler = wordHandler()

    def startGame(self):
        print("### Welcome to the Jumper Game ###")
        while(self.lives > 0):
            
