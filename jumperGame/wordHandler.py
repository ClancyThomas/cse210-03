from random import randint

class wordHandler:
    
    def __init__(self):
        self._secretWord = ""
        self._wordList = ["alphabet", "couch", "potato", "garden", "television", "belly", "pants", "mirror", "university"]

    # Randomly selects the secret word
    def createSecretWord(self):
        x = len(self._wordList)
        randomIndex = randint(0, x-1)
        self._secretWord = self._wordList[randomIndex]

    # Returns the secret word
    def getSecretWord(self):
        return self._secretWord
