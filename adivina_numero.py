def jugar():

    """import random"""
    import random
    print("************************************")
    print("    Adivina el numero    ")
    print("************************************")

    print("Elige el nivel de dificultad")
    print("(1) Novato (2) Intermedio (3) Avanzado")


    nivel = int(input("Nivel: "))

    if nivel == 1:
        total_intentos = 20
    elif nivel == 2:
        total_intentos = 10
    else:
        total_intentos = 5



    #numero_secreto = round(random.random()*100)
    numero_secreto = random.randint(1,100)
    puntos = 1000
    #print("El numero secreto es: ", numero_secreto)
    #Mientras se cumpla condicion , continue ejecutando
    #total_intentos = 3
    #intento = 1 


    #while (total_intentos >= intento):
    for intento in range(1,total_intentos+1):
        #print("Intento {} de {}".format(intento, total_intentos))
        print(f"Intento {intento} de {total_intentos}")
        
        # Introducir un numero
        entrada_str = input("Digita un numero: ")
        entrada = int(entrada_str)
        if (entrada < 1 or entrada > 100):
            print("Digita un numero mayor que 0 y menor o igual a 100")
            continue
        print("El numero que digitaste: ",entrada)

        acierto = entrada == numero_secreto
        mayor = entrada > numero_secreto
        menor = entrada < numero_secreto

        #Si numero entrada es igual a numero secreto: acierto
        if acierto:
            print(f"Has acertado! tu puntaje es {puntos}")
            break
        #Si no se cumple, sera: Error
        else:
        #Si el usuario digito un numero mayor entonces especificar
            if mayor:
                print("El numero no corresponde! El numero que ingresaste es mayor.")
            elif menor:
                print("El numero no corresponde! El numero que ingresaste es menor.")
        #intento += 1
            puntos_perdidos =abs(numero_secreto - entrada)
            puntos = puntos - puntos_perdidos

    print("El juego ha concluido")
if (__name__=="__main__"):
    jugar()
