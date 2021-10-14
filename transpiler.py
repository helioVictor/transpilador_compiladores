import json
from FileHandler import FileHandler
from helpers import organizeBrackets, tokenizer
from converters import handleTokensConversion

def transpiler(sourceFile, destinationFile):
    # print(f'source file: {sourceFile}')
    # print(f'O que tem no arquivo fonte: {sourceFile.readFile()}')
    sourceTokens = tokenizer(sourceFile.readFile())
    sourceBrackets = organizeBrackets(sourceTokens)
    destinationTokens = []

    print(sourceFile)

    portugolReservedWordsFile = open('portugolReservedWords.json')
    pythonReservedWordsFile = open('pythonReservedWords.json')
    
    portugolReservedWords = json.load(portugolReservedWordsFile)
    pythonReservedWords = json.load(pythonReservedWordsFile)

    # print(sourceTokens)
    handleTokensConversion(sourceTokens, destinationTokens, portugolReservedWords, pythonReservedWords)
    
    print(destinationTokens)
    destinationFile.writeFile(destinationTokens)
    # print(f'destination file: {destinationFile}')
    # print(f'destination file: {destinationFile.writeFile()}')