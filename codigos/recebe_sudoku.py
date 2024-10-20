def exibe_matriz(matriz):
    """
    """
    n = len(matriz[0])
    m = len(matriz)
    for i in range (0,n):
        print()
        for j in range (0,m):
            print(f'{matriz[i][j]}', end = ' ')

def cria_matriz(n = 9, m = 9):
    """
    Obj -   Construir uma matriz n x m

    parâmetros
    n = número de linhas 
    m = número de colunas

    retorno - retorna a matriz com os valores de cada célula definidos como ij.
    """

    matriz = []
    vetor = []
    for i in range (0,n):
        for j in range (0,m):
            vetor.append(((i + 1) * 10) + (j + 1))
        matriz.append(vetor[:])
        vetor.clear()
    
    return matriz


matriz = cria_matriz()
exibe_matriz(matriz)