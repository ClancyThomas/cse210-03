from parachute import Image
from guessHandler import guessHandler
from wordHandler import wordHandler
from terminalService import terminalService

class director:

    def __init__(self):
        self.lives = 5
        self.parachute = Image()
        self.guessHandler = guessHandler()
        self.wordHandler = wordHandler()
        self.terminalService = terminalService()

    def startGame(self):
        print("### Welcome to the Jumper Game ###")
        
        self.wordHandler.createSecretWord()
        word = self.wordHandler.getSecretWord()
        self.guessHandler.setupGuess()

        while(self.lives > 0):
            self.parachute.updateParachute()
            
            self.terminalService.printGame(self.guessHandler.progress, self.parachute.image)
            
            self.guessHandler.newGuess()
            if (self.guessHandler.checkGuess()):
                continue
            else:
                self.lives -=1
            
            
