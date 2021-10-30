class FileHandler:
    def __init__(self, filename='example'):
        self.filename = filename

    def readWholeFile(self):
        with open(f'{self.filename}.txt', mode='r') as file:
            lines = file.read()
        return lines

    def readFile(self):
        with open(f'{self.filename}.txt') as file:
            lines = file.readlines()
        return lines
    
    def writeFile(self, fileLines = ['print("Jefter")\n', 'print("Tiago")\n']):
        with open(f'{self.filename}.py', 'w') as file:
            for line in fileLines:
                file.write(line)