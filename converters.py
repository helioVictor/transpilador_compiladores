def handleBaseConversion(
    index,
    sourceTokens,
    sourceTokensWithoutSpaces,
    destinationTokens,
    portugolReservedWords,
    pythonReservedWords,
    keywordsPositions,
    blocksArray
):  
    # print(f'f{index} - {sourceTokensWithoutSpaces[index]}')
    if(sourceTokensWithoutSpaces[index-1] == portugolReservedWords['variable']):
        destinationTokens.append(sourceTokens[index])
        if (sourceTokensWithoutSpaces[index + 1] == '='):
            destinationTokens.append(' = ')
            if(
                sourceTokensWithoutSpaces[index + 3] == '+' or
                sourceTokensWithoutSpaces[index + 3] == '-' or
                sourceTokensWithoutSpaces[index + 3] == '*' or
                sourceTokensWithoutSpaces[index + 3] == '/'
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
    # print(f'key - {keywordsPositions}')
    # print(f'blocks - {blocksArray}')
    for index in range(len(sourceTokensWithoutSpaces)):
        # print(f'{index} - {sourceTokens[index]}')
        # print(f'w{index} - {sourceTokensWithoutSpaces[index]}')
        # print(keywordsPositions)
        # print(blocksArray)
        # if (index > blocksArray[blocksCounter][0] and 
        #     index < blocksArray[blocksCounter][1]
        # ):
        #     print(blocksArray[blocksCounter][0])
        #     print(blocksCounter)
        #     print(index)
        #     destinationTokens.append('\t')
        # if (index >= keywordsPositions[blocksCounter][1] and 
        #     keywordsPositions[blocksCounter][0] == portugolReservedWords['while'] and
        #     index < blocksArray[blocksCounter][0]
        # ):  
        #     if sourceTokens[index] == portugolReservedWords['while']:
        #         destinationTokens.append(pythonReservedWords['while'])
        #     else:
        #         destinationTokens.append(sourceTokens[index])
        # if index == blocksArray[blocksCounter][0]:
        #         destinationTokens.append(':\n')
        # if (sourceTokens[index] == portugolReservedWords['while']):
        #     destinationTokens.append(pythonReservedWords['while'])
        #     cont = 1
        #     while(sourceTokens[index + cont] != '{'):
        #         destinationTokens.append(sourceTokens[index + cont])
        #         cont += 1
        #     destinationTokens.append(':\n')
        # if (sourceTokens[index] == portugolReservedWords['if']):
        #     destinationTokens.append(pythonReservedWords['if'])
        #     cont = 1
        #     while(sourceTokens[index + cont] != '{'):
        #         destinationTokens.append(sourceTokens[index + cont])
        #         cont += 1
        #     destinationTokens.append(':\n')
        # if (sourceTokens[index-1] == '{'):
        #     cont = 1
        #     while(sourceTokens[index + cont] != '}'):
        #         destinationTokens.append('\t')
        #         cont += 1
        #     blocksCounter += 1
        if (
            sourceTokensWithoutSpaces[index] == pythonReservedWords['while'] or
            sourceTokensWithoutSpaces[index] == pythonReservedWords['if'] or
            sourceTokensWithoutSpaces[index] == pythonReservedWords['elif'] or
            sourceTokensWithoutSpaces[index] == pythonReservedWords['else']
        ):  
            if (sourceTokensWithoutSpaces[index] == pythonReservedWords['while']):
                destinationTokens.append('\n')
            
            destinationTokens.append(sourceTokens[index])
            destinationTokens = handleBaseConversion(
                index,
                sourceTokens,
                sourceTokensWithoutSpaces,
                destinationTokens,
                portugolReservedWords,
                pythonReservedWords,
                keywordsPositions,
                blocksArray
            )
            blocksCounter += 1
        
        # print(f'counter{blocksCounter}')
        # print(f'keyword{keywordsPositions[blocksCounter][1]}')

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
            pythonReservedWords,
            keywordsPositions,
            blocksArray
        )
        # if(
        #     sourceTokensWithoutSpaces[index-1] == portugolReservedWords['variable']
        # ):
        #     destinationTokens.append(sourceTokens[index])
        #     if (sourceTokensWithoutSpaces[index + 1] == '='):
        #         destinationTokens.append(' = ')
        #         if(
        #             sourceTokensWithoutSpaces[index + 3] == '+' or
        #             sourceTokensWithoutSpaces[index + 3] == '-' or
        #             sourceTokensWithoutSpaces[index + 3] == '*' or
        #             sourceTokensWithoutSpaces[index + 3] == '/'
        #         ):
        #             destinationTokens.append(f'{sourceTokens[index + 2]}')
        #             destinationTokens.append(f' {sourceTokens[index + 3]} ')
        #             destinationTokens.append(f'{sourceTokens[index + 4]}\n')
        #         elif(
        #             sourceTokensWithoutSpaces[index + 3] == pythonReservedWords['operators']['and'] or
        #             sourceTokensWithoutSpaces[index + 3] == pythonReservedWords['operators']['or'] or
        #             sourceTokensWithoutSpaces[index + 3] == pythonReservedWords['operators']['difference'] or
        #             sourceTokensWithoutSpaces[index + 3] == pythonReservedWords['operators']['equal']
        #         ):  
        #             destinationTokens.append(f'{sourceTokens[index + 2]}')
        #             destinationTokens.append(f' {sourceTokens[index + 3]} ')
        #             destinationTokens.append(f'{sourceTokens[index + 4]}\n')
        #         else:
        #             destinationTokens.append(sourceTokens[index+2] + '\n')
        # if(sourceTokens[index-1] == portugolReservedWords['input']):
        #     destinationTokens.append(sourceTokens[index])
        #     destinationTokens.append(' = ')
        #     destinationTokens.append(pythonReservedWords['input'] + '()' + '\n')
        # if(sourceTokensWithoutSpaces[index-1] == pythonReservedWords['print']):
        #     destinationTokens.append(sourceTokens[index - 1] + f'({sourceTokens[index]})' + '\n') 
    return destinationTokens