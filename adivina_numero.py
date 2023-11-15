print("************************************")
print("           Adivina el numero    ")
print("************************************")


numero_secreto = 55
#Mientras se cumpla condicion , continue ejecutando
total_intentos = 3
#intento = 1 


#while (total_intentos >= intento):
for intento in range(1,4):
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
        print("Has acertado")
        break
    #Si no se cumple, sera: Error
    else:
    #Si el usuario digito un numero mayor entonces especificar
        if mayor:
            print("El numero no corresponde! El numero que ingresaste es mayor.")
        elif menor:
            print("El numero no corresponde! El numero que ingresaste es menor.")
    #intento += 1

print("El juego ha concluido")

