import re

def tokenizer(LinesArray, splitter = ' '):
    tokens = []
    for line in LinesArray:
        lineArray = line.replace('\n', '').split(splitter)
        for token in lineArray:
            if token != '':
                tokens.append(token)

    return tokens

def findAll(target, fileString):
    positionsArray = []
    lastMatchPosition = 0
    while True:
        position = fileString.find(target, lastMatchPosition)
        if position == -1:
            break
        lastMatchPosition = position + 1
        positionsArray.append(position)

    return positionsArray

def symbolsDictionary(symbolsArray, fileString):
    dict = {}
    for index in range(len(symbolsArray)):
        # print(index)
        # print(symbolsArray[index])
        symbolsPositions = findAll(symbolsArray[index],fileString)
        # print(symbolsPositions)
        dict[symbolsArray[index]] = symbolsPositions
    return dict

def organizeBrackets(TokenArray):
    for index in range(len(TokenArray)):
        print(f'[{index}] - {TokenArray[index]}')
