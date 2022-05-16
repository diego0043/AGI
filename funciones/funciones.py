import random

def generadorNumero():
    n1 = random.randrange(1, 9, 1)
    n2 = random.randrange(1, 9, 1)
    n3 = random.randrange(1, 9, 1)
    resultado = str(n1) + str(n2) + str(n3)
    return resultado

def adivinarNumero(numero, numeroUser):
    num = int(numero)
    num2 = int(numeroUser)
    if num == num2:
        return True
    else:
        return False
    

