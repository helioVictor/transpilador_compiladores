def handleBaseConversion(
    index,
    sourceTokens,
    sourceTokensWithoutSpaces,
    destinationTokens,
    portugolReservedWords,
    pythonReservedWords
):
    if(sourceTokensWithoutSpaces[index-1] == portugolReservedWords['variable']):
        destinationTokens.append(sourceTokens[index])
        if (sourceTokensWithoutSpaces[index + 1] == '='):
            destinationTokens.append(' = ')
            if(
                sourceTokensWithoutSpaces[index + 3] == '+' or
                sourceTokensWithoutSpaces[index + 3] == '-' or
                sourceTokensWithoutSpaces[index + 3] == '*' or
                sourceTokensWithoutSpaces[index + 3] == '/' or
                sourceTokensWithoutSpaces[index + 3] == '**'
            ):
                destinationTokens.append(f'{sourceTokens[index + 2]}')
                destinationTokens.append(f' {sourceTokens[index + 3]} ')
                destinationTokens.append(f'{sourceTokens[index + 4]}\n')
            elif(
                sourceTokensWithoutSpaces[index + 3] == pythonReservedWords['operators']['and'] or
                sourceTokensWithoutSpaces[index + 3] == pythonReservedWords['operators']['or'] or
                sourceTokensWithoutSpaces[index + 3] == pythonReservedWords['operators']['difference'] or
                sourceTokensWithoutSpaces[index + 3] == pythonReservedWords['operators']['equal']
            ):  
                destinationTokens.append(f'{sourceTokens[index + 2]}')
                destinationTokens.append(f' {sourceTokens[index + 3]} ')
                destinationTokens.append(f'{sourceTokens[index + 4]}\n')
            else:
                destinationTokens.append(sourceTokens[index+2] + '\n')
    if(sourceTokensWithoutSpaces[index - 1] == pythonReservedWords['input']):
        if(
            sourceTokensWithoutSpaces[index] == pythonReservedWords['types']['int'] or
            sourceTokensWithoutSpaces[index] == pythonReservedWords['types']['float'] or
            sourceTokensWithoutSpaces[index] == pythonReservedWords['types']['str'] 
        ):
            destinationTokens.append(sourceTokens[index + 1])
            destinationTokens.append(' = ')
            destinationTokens.append(f'{sourceTokens[index]}({pythonReservedWords["input"]}())\n')
        else:
            destinationTokens.append(sourceTokens[index])
            destinationTokens.append(' = ')
            destinationTokens.append(pythonReservedWords['input'] + '()' + '\n')
    if(sourceTokensWithoutSpaces[index-1] == pythonReservedWords['print']):
        destinationTokens.append(sourceTokens[index - 1] + f'({sourceTokens[index]})' + '\n')
    
    return destinationTokens

def handleTokensConversion(
    sourceTokens,
    sourceTokensWithoutSpaces,
    destinationTokens,
    portugolReservedWords,
    pythonReservedWords,
    keywordsPositions,
    blocksArray
):  
    blocksCounter = -1
    for index in range(len(sourceTokensWithoutSpaces)):
        if (
            sourceTokensWithoutSpaces[index] == pythonReservedWords['while'] or
            sourceTokensWithoutSpaces[index] == pythonReservedWords['if'] or
            sourceTokensWithoutSpaces[index] == pythonReservedWords['elif'] or
            sourceTokensWithoutSpaces[index] == pythonReservedWords['else']
        ):  
            if (sourceTokensWithoutSpaces[index] == pythonReservedWords['while']):
                destinationTokens.append('\n')
            
            destinationTokens.append(sourceTokens[index] + ' ')
            destinationTokens = handleBaseConversion(
                index,
                sourceTokens,
                sourceTokensWithoutSpaces,
                destinationTokens,
                portugolReservedWords,
                pythonReservedWords
            )
            blocksCounter += 1
        

        if (len(keywordsPositions) > 0 and len(blocksArray) > 0):
            if (
                index > keywordsPositions[blocksCounter][1] and
                index < blocksArray[blocksCounter]
            ):
                destinationTokens.append(f'{sourceTokens[index]}')

            if (sourceTokensWithoutSpaces[index] == ':\n'):
                destinationTokens.append(f'{sourceTokens[index]}')
            
        destinationTokens = handleBaseConversion(
            index,
            sourceTokens,
            sourceTokensWithoutSpaces,
            destinationTokens,
            portugolReservedWords,
            pythonReservedWords
        )
       
    return destinationTokens