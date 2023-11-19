"""Init game horca"""

def jugar():
    """titles for game"""
    print("************************************")
    print("    Juego de la Horca - Bienvenido   ")
    print("************************************")
    print("Elige el nivel de dificultad")
    print("(1) Novato (2) Intermedio (3) Avanzado")

palabra_secreta = "fresa".upper()
palabra_secreta = palabra_secreta.strip()
letras_acertadas = ['_' for letra in palabra_secreta]
print(letras_acertadas)

# Mientras la persona no se ahorque ni acierte la palabra el juego continua
ahorco = False
acerto = False
errores = 0

while (not ahorco and not acerto):
    intento = input("\nDigita una letra: ")
    intento = intento.strip().upper()
    if intento in palabra_secreta:
        indice = 0

        for letra in palabra_secreta:
            if intento == letra:
                letras_acertadas[indice] = letra
                #print("Encontre la letra '{letra}' en la posicion {indice}")
            indice = indice + 1
    else:
        errores += 1
        #print("¡Ups, has fallado! Quedan {} intentos.".format(6-errores))
    ahorco = errores == 6
    acerto = '_' not in letras_acertadas
    print(letras_acertadas)
    if ahorco:
        print("\nPerdiste el juego")
    elif acerto:
        print("\nGanaste el juego")



print("\nFin del juego")


if (__name__=="__main__"):
    jugar()