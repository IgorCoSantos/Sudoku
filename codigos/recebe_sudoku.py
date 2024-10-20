def exibe_matriz(matriz):
    """
    Obj - exibir a matriz na forma expandida

    parâmetros
    matriz - matriz a ser exibida

    retorno - print da matriz em sua forma expandida
    """
    n = len(matriz[0])
    m = len(matriz)
    tam = 0

    # Legenda das colunas (parte superior)

    for x in range (1, m+1):

        if x == 1:
            print(' '*4, end = '')
            print(f'{' '*2}{x}', end = '')

        elif x == m:
            print(f'{' '*2}{x}', end = '\n')

        else:
            print(f'{' '*2}{x}', end = '')

    print(f'{' '*4}{'='*(3*m)}{'='*2}')

    #Exibição da matriz

    for i in range (0,n):

        for j in range (0,m):

            # Legenda das linhas (parte esquerda)

            if j == 0:
                print(f'{i+1}', end = '  | ')

                if i in [0,1,2,6,7,8]:
                    fundo_branco('', ' ')
                else:
                    print(f'', end = ' ')
            
            if i in [0,1,2] and j in [0,1,2]\
            or i in [0,1,2] and j in [6,7,8]\
            or i in [3,4,5] and j in [3,4,5]\
            or i in [6,7,8] and j in [0,1,2]\
            or i in [6,7,8] and j in [6,7,8]:

                #new
                if j == m-1:
                    fundo_branco(matriz[i][j], ' ')
                    print(' |')

                elif j == 5 or j==2:
                    fundo_branco(matriz[i][j], ' ')
                    print(f'', end = ' ')

                else:
                    fundo_branco(matriz[i][j], '  ')

            else:

                if j == m-1:
                    print(f'{matriz[i][j]}', end = '  |\n')

                elif j in [2,5]:
                    print(f'{matriz[i][j]}', end = ' ')
                    fundo_branco('', ' ')

                else:
                    print(f'{matriz[i][j]}', end = '  ')

            if i == n-1:
                tam += (len(str(matriz[i][j])) + 2)

    # Legenda das colunas (parte superior)

    print(f'{' '*4}{'='*(3*m)}{'='*2}')

def cria_matriz(n = 9, m = 9):

    """
    Obj -   Construir uma matriz n x m

    parâmetros
    n = número de linhas 
    m = número de colunas

    retorno - retorna a matriz 
    """

    matriz = []
    vetor = []

    for i in range (0,n):

        for j in range (0,m):
            vetor.append((j + 1))

        matriz.append(vetor[:])
        vetor.clear()
    
    return matriz

def fundo_branco(texto, end = '\n'):

    from colorama import Back, Style

    print(Back.WHITE + f'{texto}', end = end + Style.RESET_ALL)


# fundo_branco(f'teste', '  ')
# print('teste')


# print(Back.WHITE + 'Este texto tem um fundo amarelo!' + Style.RESET_ALL)
# print(Back.WHITE + f'{'teste'}'+ Style.RESET_ALL)


matriz = cria_matriz()
exibe_matriz(matriz)