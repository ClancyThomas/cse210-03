from random import randint

class wordHandler:
    
    def __init__(self):
        self.secretWord = ""
        self.wordList = ["alphabet", "couch", "potato", "garden", "television", "belly", "pants", "mirror", "university"]

    def createSecretWord(self):
        x = len(self.wordList)
        randomIndex = randint(0, x-1)
        self.secretWord = self.wordList[randomIndex]

    def getSecretWord(self):
        return self.secretWord
