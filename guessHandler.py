class guessHandler:

    def __init__(self):
        self.guess = ""
        self.progress = ""

    def setupGuess(self, secretWord):
        wordLen = len(secretWord)
        for i in range(0, wordLen):
            self.progress += "_"

    def newGuess(self):
        guess = input("Guess a lette from A to Z: ")
        self.guess = guess.lower()

    def checkGuess(self, secretWord):
        wordLen = len(secretWord)
        for i in range(0, wordLen):
            if self.guess == secretWord[i]:
                self.progress[i] = secretWord[i]
        
            

