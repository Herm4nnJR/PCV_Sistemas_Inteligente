import random

# Define as dimensões da matriz
linhas = 500
colunas = 500

# Cria uma matriz preenchida com zeros
matriz = [[0 for j in range(colunas)] for i in range(linhas)]

# Preenche a matriz com números aleatórios entre 0 e 9
for i in range(linhas):
    for j in range(i, colunas):
        if i == j:
            matriz[i][j] = 0
        elif i == j-1 or (i == 0 and j == colunas - 1) :
            matriz[i][j] = 5
            matriz[j][i] = 5
        else:
            matriz[i][j] = random.randint(10, 100)
            matriz[j][i] = matriz[i][j]

# Salva a matriz em um arquivo de texto
with open('matriz500.txt', 'w') as arquivo:
    for i in range(linhas):
        linha = ','.join(str(x) for x in matriz[i])
        arquivo.write(linha + '\n')
