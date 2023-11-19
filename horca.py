"""Init game horca"""

def jugar():
    """titles for game"""
    print("************************************")
    print("    Juego de la Horca - Bienvenido   ")
    print("************************************")
    print("Elige el nivel de dificultad")
    print("(1) Novato (2) Intermedio (3) Avanzado")

palabra_secreta = "banana"
palabra_secreta = palabra_secreta.strip()
letras_acertadas = ['_','_','_','_','_','_']
print(letras_acertadas)

# Mientras la persona no se ahorque ni acierte la palabra el juego continua
ahorco = False
acerto = False

while (not ahorco and not acerto):
    intento = input("\nDigita una letra: ")
    intento = intento.strip()
    indice = 0
    for letra in palabra_secreta:
        if intento.upper() == letra.upper():
            letras_acertadas[indice] = letra.upper()
            #print("Encontre la letra '{letra}' en la posicion {indice}")
        indice = indice + 1
    print(letras_acertadas)



print("Fin del juego")


if (__name__=="__main__"):
    jugar()