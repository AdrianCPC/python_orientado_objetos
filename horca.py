def jugar():

    print("************************************")
    print("    Juego de la Horca - Bienvenido   ")
    print("************************************")
    print("Elige el nivel de dificultad")
    print("(1) Novato (2) Intermedio (3) Avanzado")

palabra_secreta = "banana"
palabra_secreta = palabra_secreta.strip()

# Mientras la persona no se ahorque ni acierte la palabra el juego continua
ahorco = False
acerto = False

while (not ahorco and not acerto):
    intento = input("Digita una letra")
    intento = intento.strip()
    indice = 0
    for letra in palabra_secreta:
        if intento.upper() == letra.upper():
            print("Encontre la letra '{letra}' en la posicion {indice}")
        indice = indice + 1
    print("Jugando")



print("Fin del juego")


if (__name__=="__main__"):
    jugar()