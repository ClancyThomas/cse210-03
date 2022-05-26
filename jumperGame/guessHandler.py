class guessHandler:

    def __init__(self):
        self.guess = ""
        self.progress = ""
        self.correct = False

    def setupGuess(self, secretWord):
        for i in range(0, len(secretWord)-1):
            self.progress += "_"

    def newGuess(self):
        guess = input("\nGuess a letter from A to Z: ")
        self.guess = guess.lower()

    def checkGuess(self, secretWord):
        self.correct = False
        for i in range(0, len(secretWord)-1):
            if self.guess == secretWord[i]:
                self.progress[i] = secretWord[i]
                self.correct = True
        return self.correct
                

        
            

