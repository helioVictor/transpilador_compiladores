import json
from FileHandler import FileHandler
from helpers import tokenizer, getBlocks, getKeywordsPosition, handleSpacesCount
from converters import handleTokensConversion

def transpiler(sourceFile, destinationFile):
    # print(f'source file: {sourceFile}')
    # print(f'O que tem no arquivo fonte: {sourceFile.readFile()}')
    # source = sourceFile.readWholeFile()
    # print(source)
    # closeBracket = findAll('}', source)
    # print(closeBracket)
    # print(symbols['{'][0])
    # print(symbols['}'][0])
    # print(symbols['('][0])
    # print(symbols[')'][0])
    #  print(symbols[0]['{'][0])
    # print(symbols[1]['}'][0])

    # print(sourceFile)

    portugolReservedWordsFile = open('portugolReservedWords.json')
    pythonReservedWordsFile = open('pythonReservedWords.json')
    
    portugolReservedWords = json.load(portugolReservedWordsFile)
    pythonReservedWords = json.load(pythonReservedWordsFile)

    sourceTokensSpaces = handleSpacesCount(sourceFile.readFile())
    sourceTokens, sourceTokensWithoutSpaces = tokenizer(sourceFile.readFile(), portugolReservedWords, pythonReservedWords, sourceTokensSpaces)
    print(sourceTokensSpaces)
    print(sourceTokens)
    print('-----------------------')
    print(f'ss: {sourceTokensWithoutSpaces}')
    # print(getKeywordsPosition(sourceTokens))
    blocksArray = getBlocks(sourceTokensWithoutSpaces)
    keywordsPositions = getKeywordsPosition(sourceTokensWithoutSpaces)
    # print(blocksArray)
    # print(keywordsPositions)
    # sourceBrackets = organizeBrackets(sourceTokens)
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
    
    print(destinationTokens)
    destinationFile.writeFile(destinationTokens)
    # print(f'destination file: {destinationFile}')
    # print(f'destination file: {destinationFile.writeFile()}')