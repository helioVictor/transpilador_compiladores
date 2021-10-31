import re

def handleTokenVerification(token, portugolReservedWords, pythonReservedWords):
    if (token == portugolReservedWords['boolean']['true']): 
        return pythonReservedWords['boolean']['true'] 

    if (token == portugolReservedWords['boolean']['false']): 
        return pythonReservedWords['boolean']['false'] 
    
    if (token == portugolReservedWords['operators']['equal']): 
        return pythonReservedWords['operators']['equal'] 
    
    if (token == portugolReservedWords['operators']['difference']): 
        return pythonReservedWords['operators']['difference'] 
    
    if (token == portugolReservedWords['operators']['and']): 
        return pythonReservedWords['operators']['and'] 
    
    if (token == portugolReservedWords['operators']['or']): 
        return pythonReservedWords['operators']['or']
    
    return token

def handleTokenManipulation(token, portugolReservedWords, pythonReservedWords):
    if (
        token[0] + token[-1] == '""' or
        token[0] + token[-1] == "''"
    ):
        token = token.replace('$', ' ')
        if token.find('{') and token.find('}'):
            token = 'f'+token
    
    return handleTokenVerification(token, portugolReservedWords, pythonReservedWords)

def tokenizer(LinesArray, portugolReservedWords, pythonReservedWords, splitter = ' '):
    tokens = []
    for line in LinesArray:
        lineArray = line.replace('\n', '').split(splitter)
        # print(lineArray)
        for token in lineArray:
            if token != '':
                token = handleTokenManipulation(token, portugolReservedWords, pythonReservedWords)
                tokens.append(token)

    return tokens

def findAll(target, tokensArray):
    positionsArray = []
    for index in range(len(tokensArray)):
        if (target == tokensArray[index]):
            positionsArray.append(index)

    return positionsArray

def getKeywordsPosition(tokensArray):
    keywordsPosition = []
    for index in range(len(tokensArray)):
        if tokensArray[index] == 'se':
            keywordsPosition.append(['se', index])

        if tokensArray[index] == 'senaose':
            keywordsPosition.append(['senaose', index])
        
        if tokensArray[index] == 'senao':
            keywordsPosition.append(['senao', index])
        
        if tokensArray[index] == 'enquanto':
            keywordsPosition.append(['enquanto', index])
    
    return keywordsPosition


def getBlocks(tokensArray, symbolsArray = ['{', '}']):
    blocksArray = []
    for index in range(len(symbolsArray)):
        if symbolsArray[index] == '{':
            openBracketsPositions = findAll(symbolsArray[index],tokensArray)
        if symbolsArray[index] == '}':
            closedBracketsPositions = findAll(symbolsArray[index],tokensArray)

    for index in range(len(openBracketsPositions)):
        pair = [openBracketsPositions[index], closedBracketsPositions[index]]
        blocksArray.append(pair)
    
    return blocksArray

def organizeBrackets(TokenArray):
    for index in range(len(TokenArray)):
        print(f'[{index}] - {TokenArray[index]}')
