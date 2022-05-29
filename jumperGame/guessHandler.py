class guessHandler:

    def __init__(self):
        self.guess = ""
        self.progress = ""
        self.correct = False

    # Starts the placeholder for guessing
    def setupGuess(self, secretWord):
        for i in range(0, len(secretWord)):
            self.progress += "_"

    # Gets a new guess
    def newGuess(self):
        valid_input = True
        while valid_input:
            guess = input("\nGuess a letter from A to Z: ")
            if guess.isalpha():
                valid_input = False
            else:
                print("\nGuess must be a letter from A to Z.")

        self.guess = guess.lower()

    # Checks if the guess exists in the word and replaces it in the placeholder
    def checkGuess(self, secretWord):
        self.correct = False
        for i in range(0, len(secretWord)):
            if self.guess.lower() == secretWord[i].lower():
                tempList = list(self.progress)
                tempList[i] = secretWord[i]
                self.progress = "".join(tempList)
                self.correct = True
        return self.correct
                

        
            

