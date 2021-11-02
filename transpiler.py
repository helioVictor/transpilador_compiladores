import json
from FileHandler import FileHandler
from helpers import tokenizer, getBlocks, getKeywordsPosition, handleSpacesCount
from converters import handleTokensConversion

def transpiler(sourceFile, destinationFile):
    portugolReservedWordsFile = open('portugolReservedWords.json')
    pythonReservedWordsFile = open('pythonReservedWords.json')
    
    portugolReservedWords = json.load(portugolReservedWordsFile)
    pythonReservedWords = json.load(pythonReservedWordsFile)

    sourceTokensSpaces = handleSpacesCount(sourceFile.readFile())
    sourceTokens, sourceTokensWithoutSpaces = tokenizer(sourceFile.readFile(), 
                                                        portugolReservedWords,
                                                        pythonReservedWords,
                                                        sourceTokensSpaces)
    blocksArray = getBlocks(sourceTokensWithoutSpaces)
    keywordsPositions = getKeywordsPosition(sourceTokensWithoutSpaces)

    destinationTokens = []

    handleTokensConversion(
        sourceTokens,
        sourceTokensWithoutSpaces,
        destinationTokens,
        portugolReservedWords,
        pythonReservedWords,
        keywordsPositions,
        blocksArray
    )
    
    destinationFile.writeFile(destinationTokens)