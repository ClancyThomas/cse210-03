from random import randint

class wordHandler:
    
    def __init__(self):
        self.secretWord = ""
        self.wordList = ["Alphabet", "Couch", "Potato", "Garden", "Television"]

    def createSecretWord(self):
        x = len(self.wordList)
        randomIndex = randint(0, x-1)
        self.secretWord = self.wordList[randomIndex]

    def getSecretWord(self):
        return self.secretWord
