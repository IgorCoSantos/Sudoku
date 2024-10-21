def exibe_matriz(matriz):
    """
    Obj - exibir a matriz na forma expandida

    parâmetros
    matriz - matriz a ser exibida

    retorno - print da matriz em sua forma expandida
    """
    n = tam_matriz_col(matriz)
    m = tam_matriz_lin(matriz)
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

def cria_matriz(n = 9, m = 9, x = 1):

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
            vetor.append((j + 1)*x)

        matriz.append(vetor[:])
        vetor.clear()
    
    return matriz

def fundo_branco(texto, end = '\n'):
    '''
    Obj - alterar a cor do fundo do texto para branco

    parâmetros
    texto - texto a ser exibido com fundo branco
    end - fim de texto

    retorno - print do texto com fundo branco
    '''
    from colorama import Back, Style

    print(Back.WHITE + f'{texto}', end = end + Style.RESET_ALL)

def inp_matriz():


    import os
    from validacao import val_zero_um, val_int

    matriz = cria_matriz(x = 0)
    m = tam_matriz_col(matriz)
    n = tam_matriz_lin(matriz)

    while True:
        
        exibe_matriz(matriz)

        x = val_int(input('Digite 1 para continuar e 0 para sair: '),[0,1])

        val_zero_um(x)

        if x == 0:
            print('Esquema do sudoku finalizado\n')
            break

        c = val_int(input('Qual o número da coluna: '), list(range(1,m+1)))
        l = val_int(input('Qual o número da linha: '), list(range(1,n+1)))
        v = val_int(input('Qual o valor da célula (1 - 9): '), list(range(1,10)))

        matriz[l-1][c-1] = v
        os.system('cls')

    return matriz

def tam_matriz_lin(matriz):

    n = len(matriz[0])

    return n

def tam_matriz_col(matriz):

    m = len(matriz)
    
    return m

matriz = inp_matriz()

# matriz = cria_matriz(x = 0)
# exibe_matriz(matriz)