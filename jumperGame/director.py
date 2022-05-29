from jumperGame.parachute import Image
from jumperGame.guessHandler import guessHandler
from jumperGame.wordHandler import wordHandler
from jumperGame.terminalService import terminalService

class director:

    def __init__(self):
        self._lives = 5
        self._parachute = Image()
        self._guessHandler = guessHandler()
        self._wordHandler = wordHandler()
        self._terminalService = terminalService()

    # Function the runs the game
    def _startGame(self):
        print("\n### Welcome to the Jumper Game ###\n")
        
        # Get the secret word and get the game setup with that word
        self._wordHandler.createSecretWord()
        secretWord = self._wordHandler.getSecretWord()
        self._guessHandler._setupGuess(secretWord)

        # Loop that will repeat while the player still has lives or they haven't guessed the word
        while(self._lives > 0 and self._guessHandler._progress != secretWord):
            
            # Update the parachute image and then print-Ask for the next guess
            self._parachute.updateParachute(self._lives)
            self._terminalService.printGame(self._parachute._image, self._guessHandler._progress)
            self._guessHandler.newGuess()

            if (self._guessHandler.checkGuess(secretWord)):
                continue
            else:
                self._lives -=1
        
        # Print the last phase of the game out for losers and print you win if they won
        if(self._lives == 0):
            self._parachute.updateParachute(self._lives)
            self._terminalService.printGame(self._parachute._image, self._guessHandler._progress)
        else:
            self._parachute.updateParachute(self._lives)
            self._terminalService.printGame(self._parachute._image, self._guessHandler._progress)
            print("\nYOU WON!!! NICE WORK!!!\n")
                
