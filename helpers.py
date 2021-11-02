def addSpacesInTheBeggining(token, spacesNumber):
    return (' ' * spacesNumber) + token


def handleTokenVerification(token, portugolReservedWords, pythonReservedWords):
   
    spacesNumber = token.count(' ')  
    token = token.replace(' ', '')
    
    if (token == portugolReservedWords['boolean']['true']): 
        return addSpacesInTheBeggining(pythonReservedWords['boolean']['true'] , spacesNumber)

    if (token == portugolReservedWords['boolean']['false']): 
        return addSpacesInTheBeggining(pythonReservedWords['boolean']['false'] , spacesNumber)
    
    if (token == portugolReservedWords['operators']['equal']): 
        return addSpacesInTheBeggining(pythonReservedWords['operators']['equal'] , spacesNumber)
    
    if (token == portugolReservedWords['operators']['difference']): 
        return addSpacesInTheBeggining(pythonReservedWords['operators']['difference'] , spacesNumber)
    
    if (token == portugolReservedWords['operators']['and']): 
        return addSpacesInTheBeggining(pythonReservedWords['operators']['and'] , spacesNumber)
    
    if (token == portugolReservedWords['operators']['or']): 
        return addSpacesInTheBeggining(pythonReservedWords['operators']['or'], spacesNumber)

    if (token == portugolReservedWords['print']): 
        return addSpacesInTheBeggining(pythonReservedWords['print'], spacesNumber)
        
    if (token == portugolReservedWords['input']): 
        return addSpacesInTheBeggining(pythonReservedWords['input'], spacesNumber)

    if (token == portugolReservedWords['if']): 
        return addSpacesInTheBeggining(pythonReservedWords['if'], spacesNumber)

    if (token == portugolReservedWords['elif']): 
        return addSpacesInTheBeggining(pythonReservedWords['elif'], spacesNumber)

    if (token == portugolReservedWords['else']): 
        return addSpacesInTheBeggining(pythonReservedWords['else'], spacesNumber)
    
    if (token == portugolReservedWords['while']): 
        return addSpacesInTheBeggining(pythonReservedWords['while'], spacesNumber)
    
    if (token == portugolReservedWords['types']['int']): 
        return addSpacesInTheBeggining(pythonReservedWords['types']['int'] , spacesNumber)

    if (token == portugolReservedWords['types']['float']): 
        return addSpacesInTheBeggining(pythonReservedWords['types']['float'], spacesNumber)
    
    if (token == portugolReservedWords['types']['str']): 
        return addSpacesInTheBeggining(pythonReservedWords['types']['str'], spacesNumber)

    token = addSpacesInTheBeggining(token, spacesNumber)

    return token

def handleTokenManipulation(token, portugolReservedWords, pythonReservedWords):
    # print(f'TOKEN: {token}')
    if token == '':
        return token
    if (
        token[0] + token[-1] == '""' or
        token[0] + token[-1] == "''"
    ):  
        token = token.replace('$', ' ')
        # print(f'depois{token}')
        # print(token.find('{')  == 1)
        # print(token.find('}'))
        if token.find('{')  == 1 and token.find('}') == 1:
            return 'f' + token
        return token
    # print(f'TOKEAN: {token}')
    return handleTokenVerification(token, portugolReservedWords, pythonReservedWords)


def handleSpacesCount(LinesArray, splitter = ' '):
    spacesArray = []
    for line in LinesArray:
        # print(line)
        lineArray = line.replace('\n', '')
        # print(lineArray)
        spaceCounter = 0
        for token in lineArray:
            if token != ' ':
                break
            spaceCounter += 1
        spacesArray.append(spaceCounter)

    return spacesArray
    
def tokenizer(LinesArray, portugolReservedWords, pythonReservedWords, spacesArray, splitter = ' '):
    tokens = []
    tokensWithoutSpaces = []
    for index in range(len(LinesArray)):
        lineArray = LinesArray[index].replace('\n', '').split(splitter)
        # print(f'1 - indexxx: {index} = {lineArray[spacesArray[index]]}')
        print(lineArray)
        lineArray[spacesArray[index]] = handleTokenManipulation(lineArray[spacesArray[index]], portugolReservedWords, pythonReservedWords)
        print(f'bla{lineArray[spacesArray[index]]}')
        print(spacesArray[index])
        # print(f'blaa{lineArray[spacesArray[index]]}')
        
        if (lineArray[spacesArray[index]] == portugolReservedWords['variable']):
            # print(f'AHHHHHH{lineArray[spacesArray[index]]}')
            lineArray[spacesArray[index] + 1] = (' ' * spacesArray[index]) + lineArray[spacesArray[index] + 1]
        if (lineArray[spacesArray[index]] == pythonReservedWords['input']):
            
            if (
                lineArray[spacesArray[index] + 1] == portugolReservedWords['types']['int'] or
                lineArray[spacesArray[index] + 1] == portugolReservedWords['types']['float'] or
                lineArray[spacesArray[index] + 1] == portugolReservedWords['types']['str']
            ):  
                lineArray[spacesArray[index] + 2] = (' ' * spacesArray[index]) + lineArray[spacesArray[index] + 2]
            else:
                print(f'bebebeb:  {spacesArray[index]}')
                lineArray[spacesArray[index] + 1] = (' ' * spacesArray[index]) + lineArray[spacesArray[index] + 1]

        else:
            lineArray[spacesArray[index]] = (' ' * spacesArray[index]) + lineArray[spacesArray[index]]
        # print(lineArray[spacesArray[index]])
        for index in range(len(lineArray)):
            if (
                lineArray[index] != '' and
                lineArray[index] != '}'
            ):  
                # print(f'AHAAHAHH{lineArray[index]}')
                lineArray[index] = handleTokenManipulation(lineArray[index], portugolReservedWords, pythonReservedWords)
                # print(f'HEHEHEHE{lineArray[index]}')
                if (lineArray[index] == '{'):
                    tokens.append(':\n')
                else:
                    tokens.append(lineArray[index])
        # print(f'2 - indexxx: {index} = {lineArray[spacesArray[index]]}')
    for token in tokens:
        tokensWithoutSpaces.append(removeSpaces(token))

    return tokens, tokensWithoutSpaces

def findAll(target, tokensArray):
    positionsArray = []
    for index in range(len(tokensArray)):
        if (target == tokensArray[index]):
            positionsArray.append(index)

    return positionsArray

def getKeywordsPosition(tokensArray):
    keywordsPosition = []
    for index in range(len(tokensArray)):
        if tokensArray[index] == 'if':
            keywordsPosition.append(['if', index])

        if tokensArray[index] == 'elif':
            keywordsPosition.append(['elif', index])
        
        if tokensArray[index] == 'else':
            keywordsPosition.append(['else', index])
        
        if tokensArray[index] == 'while':
            keywordsPosition.append(['while', index])
    
    return keywordsPosition


def getBlocks(tokensArray, symbolsArray = [':\n']):    
    return findAll(symbolsArray[0],tokensArray)

def removeSpaces(token):
    return token.replace(' ', '')
