from jumperGame.parachute import Image
from jumperGame.guessHandler import guessHandler
from jumperGame.wordHandler import wordHandler
from jumperGame.terminalService import terminalService

class director:

    def __init__(self):
        self.lives = 5
        self.parachute = Image()
        self.guessHandler = guessHandler()
        self.wordHandler = wordHandler()
        self.terminalService = terminalService()

    def startGame(self):
        print("\n### Welcome to the Jumper Game ###\n")
        
        self.wordHandler.createSecretWord()
        secretWord = self.wordHandler.getSecretWord()
        self.guessHandler.setupGuess(secretWord)

        while(self.lives > 0):
            self.parachute.updateParachute(self.lives)
            
            self.terminalService.printGame(self.parachute.image, self.guessHandler.progress)
            
            self.guessHandler.newGuess()
            if (self.guessHandler.checkGuess(secretWord)):
                continue
            else:
                self.lives -=1
        
        if(self.lives == 0):
            self.parachute.updateParachute(self.lives)
            self.terminalService.printGame(self.parachute.image, self.guessHandler.progress)
        else:
            print("\nYOU WON!!! Nice work!!!")
                
