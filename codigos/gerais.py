def qtd_sudoku(arquivo):
    """
    Fornece a quantidade de sudokus na matriz de armazenamento em json

    Args:
        arquivo (path): caminho do arquivo

    Returns:
        tam: quantidade de matrizes
    """
    import json
    import os

    if os.path.exists(arquivo):
        with open(arquivo, 'r') as arq:
            matrizes = json.load(arq)
            tam = len(matrizes)
    else:
        print('Arquivo não existe')
        tam = 0
    
    return tam


def le_sudoku(arquivo):
    """
    Leitura das matrizes/sudokus armazenadas

    Args:
        arquivo (path): caminho do arquivo

    Returns:
        matriz de sudokus: retorna a lista com as matrizes armazenadas
    """
    import json

    with open(arquivo, 'r') as arq:
        retorno = json.load(arq)

    return retorno


def armazena_sudoku(matriz, arquivo):
    """
    Armazena os sudokus em uma lista num arquivo json

    Args:
        matriz (listas aninhadas): matriz do sudoku
        arquivo (path): caminho do arquivo json
    """
    import json
    import os

    if os.path.exists(arquivo):

        with open(arquivo, 'r') as arq:
            matrizes = json.load(arq)
    else:

        matrizes = []

    matrizes.append(matriz)

    with open(arquivo, 'w') as arq:
        json.dump(matrizes, arq, indent=4)

