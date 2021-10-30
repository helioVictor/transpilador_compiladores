import os.path
from FileHandler import FileHandler
from transpiler import transpiler
# filename = input('Nome do arquivo (.txt) \nDigite o nome: ')
filename = 'example'

if not os.path.isfile(f'{filename}.txt'):
    print('Arquivo não encontrado.')
else:
    sourceFile = FileHandler(filename)
    destinationFile = FileHandler(filename)

    transpiler(sourceFile, destinationFile)