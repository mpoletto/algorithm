#!/usr/bin/python3

def ourSum(lower, upper, margin = 0):
    """ 
    Retorn a soma dos números do menor para o maior, 
    e mostra um traço dos argumentos e valores de retorno 
    em cada ligação
    """
    blanks = " " * margin
    # print(blanks, lower, upper)
    if lower > upper:
        print(blanks, lower, upper, 0)
        return 0
    else:
        result = lower + ourSum(lower + 1, upper, margin + 4)
        print(blanks, lower, upper, result)
        return result
    
print(ourSum(1, 4))