class guessHandler:

    def __init__(self):
        self.guess = ""
        self.progress = ""
        self.correct = False

    def setupGuess(self, secretWord):
        wordLen = len(secretWord)
        for i in range(0, wordLen):
            self.progress += "_"

    def newGuess(self):
        guess = input("Guess a lette from A to Z: ")
        self.guess = guess.lower()

    def checkGuess(self, secretWord):
        self.correct = False
        for i in range(0, len(secretWord)):
            if self.guess == secretWord[i]:
                self.progress[i] = secretWord[i]
                self.correct = True
        return self.correct
                

        
            

