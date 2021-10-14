import re

def tokenizer(LinesArray, splitter = ' '):
    tokens = []
    for line in LinesArray:
        lineArray = line.replace('\n', '').split(splitter)
        for token in lineArray:
            if token != '':
                tokens.append(token)

    return tokens

def organizeBrackets(TokenArray):
    for index in range(len(TokenArray)):
        print(f'[{index}] - {TokenArray[index]}')
