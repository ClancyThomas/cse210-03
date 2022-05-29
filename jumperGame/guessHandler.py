class guessHandler:

    def __init__(self):
        self._guess = ""
        self._progress = ""
        self._correct = False

    # Starts the placeholder for guessing
    def _setupGuess(self, secretWord):
        for i in range(0, len(secretWord)):
            self._progress += "_"

    # Gets a new guess
    def newGuess(self):
        _valid_input = True
        while _valid_input:
            self._guess = input("\nGuess a letter from A to Z: ")
            if self._guess.isalpha():
                _valid_input = False
            else:
                print("\nGuess must be a letter from A to Z.")

        self._guess = self._guess.lower()

    # Checks if the guess exists in the word and replaces it in the placeholder
    def checkGuess(self, secretWord):
        self._correct = False
        for i in range(0, len(secretWord)):
            if self._guess.lower() == secretWord[i].lower():
                tempList = list(self._progress)
                tempList[i] = secretWord[i]
                self._progress = "".join(tempList)
                self._correct = True
        return self._correct
                

        
            

