from fileInputHandler import FileHandler

def transpiler(sourceFile, destinationFile):
    print(f'source file: {sourceFile}')
    print(f'O que tem no arquivo fonte: {sourceFile.readFile()[0]}')
    print(f'destination file: {destinationFile}')
    print(f'destination file: {destinationFile.writeFile()}')