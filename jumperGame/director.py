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

    # Function the runs the game
    def startGame(self):
        print("\n### Welcome to the Jumper Game ###\n")
        
        # Get the secret word and get the game setup with that word
        self.wordHandler.createSecretWord()
        secretWord = self.wordHandler.getSecretWord()
        self.guessHandler.setupGuess(secretWord)

        # Loop that will repeat while the player still has lives or they haven't guessed the word
        while(self.lives > 0 and self.guessHandler.progress != secretWord):
            
            # Update the parachute image and then print-Ask for the next guess
            self.parachute.updateParachute(self.lives)
            self.terminalService.printGame(self.parachute.image, self.guessHandler.progress)
            self.guessHandler.newGuess()

            if (self.guessHandler.checkGuess(secretWord)):
                continue
            else:
                self.lives -=1
        
        # Print the last phase of the game out for losers and print you win if they won
        if(self.lives == 0):
            self.parachute.updateParachute(self.lives)
            self.terminalService.printGame(self.parachute.image, self.guessHandler.progress)
        else:
            self.parachute.updateParachute(self.lives)
            self.terminalService.printGame(self.parachute.image, self.guessHandler.progress)
            print("\nYOU WON!!! Nice work!!!\n")
                
