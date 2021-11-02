import os.path
from FileHandler import FileHandler
from transpiler import transpiler

helper = f'''
    {100 * '-'}

    REGRAS DA LINGUAGEM

        1 - Use espaços para separar parâmetros

            Exemplo: 
                leia nome

        2 - Tenha boas práticas como identação correta

            Exemplo:
                se idade == 10 {'{'}
                    escreval 'parabéns!'
                {'}'}

        3 - Use '$' para delimitar as cadeias de caracteres

            Exemplo: 
                'Um$exemplo$de$uso'

        3 - Use 'variavel' antes do nome da variável para atribuição

            Exemplo: 
                variavel nome = 'sebastião'
    
    {100 * '-'}

    PALAVRAS-CHAVE

       • escreval [valor] - mostra no terminal o que deve ser escrito

       • leia (tipo - opcional) [variavel] - mostra no terminal o que deve ser escrito
            [ Tipos - inteiro | real | caractere ] (Padrão - caractere)
        
       • se | senaose | senao - estrutura de condicionais
        
       • enquanto - Laço de repetição
        
       • variavel [nomeDaVariavel] - declara uma variavel dinâmica

    Operadores booleanos
    
       • [verdadeiro | falso] - valores booleanos
        
       • igual - verifica se os valores são iguais
        
       • diferente - verifica se os valores são diferentes
        
       • e | ou - operadores lógico

    {100 * '-'}

'''
print(helper)
filename = input('Nome do arquivo (.txt) \nDigite o nome: ')

if filename[-4] == '.':
    filename = filename[:-4]

if not os.path.isfile(f'{filename}.txt'):
    print('Arquivo não encontrado.')
else:
    sourceFile = FileHandler(filename)
    destinationFile = FileHandler(filename)
    try:
        transpiler(sourceFile, destinationFile)
        print(f'\nArquivo gerado --> {filename}.py')
        print('\nArquivo convertido com sucesso!')
    except:
        print('\nOPA! Ocorreu um erro!')