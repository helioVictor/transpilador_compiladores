def handleOperatorsChoice(operator, pythonReservedWords):
    resolvedOperator = ''
    if(operator == 'igual'):
        resolvedOperator = pythonReservedWords['operators']['equal']
    if(operator == 'diferente'):
        resolvedOperator = pythonReservedWords['operators']['difference']
    if(operator == 'e'):
        resolvedOperator = pythonReservedWords['operators']['and']
    if(operator == 'ou'):
        resolvedOperator = pythonReservedWords['operators']['or']
        
    return resolvedOperator

def handleTokensConversion(
    sourceTokens,
    destinationTokens,
    portugolReservedWords,
    pythonReservedWords
):  
    for index in range(len(sourceTokens)):
        # print(f'{index} - {sourceTokens[index]}')
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
                else:
                    destinationTokens.append(sourceTokens[index+2] + '\n')
        if(sourceTokens[index-1] == portugolReservedWords['input']):
            destinationTokens.append(sourceTokens[index])
            destinationTokens.append(' = ')
            destinationTokens.append(pythonReservedWords['input'] + '()' + '\n')
        if(sourceTokens[index-1] == portugolReservedWords['print']):
            destinationTokens.append(pythonReservedWords['print'] + f'({sourceTokens[index]})' + '\n')
        if(
            sourceTokens[index] == portugolReservedWords['if'] and
            sourceTokens[index+4] == '{'
        ):  
            if(
                    sourceTokens[index + 2] == 'e' or
                    sourceTokens[index + 2] == 'ou' or
                    sourceTokens[index + 2] == 'diferente' or
                    sourceTokens[index + 2] == 'igual'
            ):  
                destinationTokens.append(f'{sourceTokens[index + 2]}')
                destinationTokens.append(f' {handleOperatorsChoice(sourceTokens[index + 3], pythonReservedWords)} ')
                destinationTokens.append(f'{sourceTokens[index + 4]}\n')
                # Fazer um while pra saber quantas casas tem antes do }

    return destinationTokens