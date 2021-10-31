def handleTokensConversion(
    sourceTokens,
    destinationTokens,
    portugolReservedWords,
    pythonReservedWords,
    keywordsPositions,
    blocksArray
):  
    blocksCounter = 0
    for index in range(len(sourceTokens)):
        print(f'{index} - {sourceTokens[index]}')
        if (index > blocksArray[blocksCounter][0] and 
            index < blocksArray[blocksCounter][1]
        ):
            print(blocksArray[blocksCounter][0])
            print(blocksCounter)
            print(index)
            destinationTokens.append('\t')
        if (index >= keywordsPositions[blocksCounter][1] and 
            keywordsPositions[blocksCounter][0] == portugolReservedWords['while'] and
            index < blocksArray[blocksCounter][0]
        ):  
            if sourceTokens[index] == portugolReservedWords['while']:
                destinationTokens.append(pythonReservedWords['while'])
            else:
                destinationTokens.append(sourceTokens[index])
        if index == blocksArray[blocksCounter][0]:
                destinationTokens.append(':\n')
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

        if(sourceTokens[index - 1] == portugolReservedWords['variable']):
            destinationTokens.append(sourceTokens[index])
            if (sourceTokens[index + 1] == '='):
                destinationTokens.append(' = ')
                if(
                    sourceTokens[index + 3] == '+' or
                    sourceTokens[index + 3] == '-' or
                    sourceTokens[index + 3] == '*' or
                    sourceTokens[index + 3] == '/'
                ):
                    destinationTokens.append(f'{sourceTokens[index + 2]}')
                    destinationTokens.append(f' {sourceTokens[index + 3]} ')
                    destinationTokens.append(f'{sourceTokens[index + 4]}\n')
                elif(
                    sourceTokens[index + 3] == pythonReservedWords['operators']['and'] or
                    sourceTokens[index + 3] == pythonReservedWords['operators']['or'] or
                    sourceTokens[index + 3] == pythonReservedWords['operators']['difference'] or
                    sourceTokens[index + 3] == pythonReservedWords['operators']['equal']
                ):  
                    destinationTokens.append(f'{sourceTokens[index + 2]}')
                    destinationTokens.append(f' {sourceTokens[index + 3]} ')
                    destinationTokens.append(f'{sourceTokens[index + 4]}\n')
                else:
                    destinationTokens.append(sourceTokens[index+2] + '\n')
        if(sourceTokens[index-1] == portugolReservedWords['input']):
            destinationTokens.append(sourceTokens[index])
            destinationTokens.append(' = ')
            destinationTokens.append(pythonReservedWords['input'] + '()' + '\n')
        if(sourceTokens[index-1] == portugolReservedWords['print']):
            destinationTokens.append(pythonReservedWords['print'] + f'({sourceTokens[index]})' + '\n') 
    return destinationTokens