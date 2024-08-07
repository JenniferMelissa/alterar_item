#lista
nomes = ['Fulano','Cicrano','Beltrano','João','Maria','José']

#exibir a lista e seus respectivos itens
for i in range(len(nomes)):
    print(f'Índice: {i}: {nomes[i]}.')

#quebra de linhas
print('\n')

try:
    #usuario informa o indice
    indice = int(input('Informa o índice a ser alterado: '))

    #faz a alteracao 
    nomes[indice] = input('Informe o novo nome: ')
except:
    print('Não foi possível fazer a alteração.')

#exibe a nova lista
for i in range(len(nomes)):
    print(f'Índice: {i}: {nomes[i]}.')