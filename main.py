from FileHandler import FileHandler
from transpiler import transpiler
# filename = input('Nome do arquivo (.txt) \nDigite o nome: ')
filename = 'example'

sourceFile = FileHandler(filename)
destinationFile = FileHandler(filename)

transpiler(sourceFile, destinationFile)
