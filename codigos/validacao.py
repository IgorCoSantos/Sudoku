def val_zero_um(x): 
    """
    Valida a inserção de um int sendo 0 ou 1

    Args:
        x : valor a ser validado
    """
    while True:
        try:
                  
                if x not in [0,1]:
                    x = int(input('Valor inválido, digite 0 ou 1: '))
                else:
                    break 
                    

        except:
                x = int(input('Valor inválido, digite 0 ou 1: '))


def val_int(x, lista = 'vazio.teste'):
    """
    valida um valor inteiro dentro de uma lista de possíveis opções

    Args:
        x : Valor a ser validado
        lista (lista): Lista com os valores permitidos para a variável a ser analisada (x). Defaults to 'vazio.teste'.

    Returns:
        x : Retorna um valor selecionado pelo usuário e dentro das condições definidas
    """
    while True:     
        
        try:
            x = float(x)

            if x % 1 == 0:
                x = int(x)
                
                if lista != 'vazio.teste':
                    if x in lista:
                        break
                    else:
                        x = input('Valor não permitido. Digite um valor inteiro dentre os permitidos: ')
                else:
                    break

            else:
                x = input('Você digitou um valor decimal. Digite um valor inteiro válido: ')

        except:
    
            x = input('Você digitou um valor não númerico. Digite um valor inteiro válido: ')
    return x





