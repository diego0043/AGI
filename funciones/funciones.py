import random


def generadorNumero():
    n1 = random.randrange(1, 9, 1)
    n2 = random.randrange(1, 9, 1)
    n3 = random.randrange(1, 9, 1)
    resultado = str(n1) + str(n2) + str(n3)
    return resultado


def adivinarNumero(numero, numeroUser):
    print(numero)

    try:

        num = int(numero)
        num2 = int(numeroUser)
        contador = 0
        arrayCoincidenciasExactas = []
        arrayCoincidenciasDiferentePosicion = []

        if num2 >= 100 and num2 < 1000:
            if num == num2:
                mensaje = "¡Felicidades!, ganaste el juego el numero era: " + numero
                salida = [True, mensaje]
                return salida
            else:
                for n in numeroUser:
                    if(numero[contador] == n):
                        arrayCoincidenciasExactas.append(n)
                    else:
                        if(numero[contador] != n):
                            arrayCoincidenciasExactas.append("")
                            if contador <= 1:
                                if numero[contador + 1] == n:
                                    arrayCoincidenciasDiferentePosicion.append(
                                        n)
                                elif numero[contador - 1] == n:
                                    arrayCoincidenciasDiferentePosicion.append(
                                        n)
                            elif contador == 2:
                                if numero[contador - 1] == n:
                                    arrayCoincidenciasDiferentePosicion.append(
                                        n)
                                elif numero[contador - 2] == n:
                                    arrayCoincidenciasDiferentePosicion.append(
                                        n)
                    contador += 1

        mensaje = "No acertaste el numero correctamente, aqui hay una pequeña ayuda :)\n\nCoincidencias Exactas:\n[ " + str(
            arrayCoincidenciasExactas[0]) + " , " + str(arrayCoincidenciasExactas[1]) + " , " + str(arrayCoincidenciasExactas[2]) + " ]\n\nCoincidencias en diferente posición:\n"

        size = len(arrayCoincidenciasDiferentePosicion) - 1
        if (size > 0):
            contador = 0
            for n in arrayCoincidenciasDiferentePosicion:
                if contador < size:
                    if contador == 0:
                        mensaje += "[ " + str(n) + ","
                    else:
                        mensaje += str(n) + ","
                else:
                    mensaje += str(n) + " ]"
                contador += 1
        else:
            mensaje += "No hay coincidencias :c"
        return [False, mensaje]

    except:
        print("Parece que ingresaste un texto en lugar de un numero o el campo esta vacio ")
