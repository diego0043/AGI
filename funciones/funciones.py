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
    
    numerosEncontrados = []
    contador = 0
    for item in numero:
        for item2 in numeroUser:
            if item2 == item:
                numerosEncontrados.append(item)
                break
        contador += 1
 
    
    if num == num2:
        mensaje = "¡Felicidades!, ganaste el juego el numero era: " + numero
        salida = [True, mensaje]
        return salida
    else:
        numeros = ""
        for numItem in numerosEncontrados:
            numeros += " ("+ str(numItem) + ") "

        mensaje = "Ups!, parece que ese no era el numero , si acertaste en una parte lo veras a continuacion: [" + numeros + "]" + " recuerda que ese no es el orden verdadero "
        salida = [True, mensaje]
        return salida
    

