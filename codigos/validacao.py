def val_zero_um(x): 

        while True:
            try:
                  
                if x not in [0,1]:
                    x = int(input('Valor inválido, digite 0 ou 1: '))
                else:
                    break 
                    

            except:
                x = int(input('Valor inválido, digite 0 ou 1: '))

def val_int(x, lista = 'vazio.teste'):
     
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





