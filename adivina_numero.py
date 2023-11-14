print("************************************")
print("           Adivina el numero    ")
print("************************************")


numero_secreto = 55

# Introducir un numero
entrada_str = input("Digita un numero: ")
entrada = int(entrada_str)
print("El numero que digitaste: ",entrada)

acierto = entrada == numero_secreto
mayor = entrada > numero_secreto
menor = entrada < numero_secreto

#Si numero entrada es igual a numero secreto: acierto
if (acierto):
    print("Has acertado")
#Si no se cumple, sera: Error
else:
#Si el usuario digito un numero mayor entonces especificar
    if (mayor):
        print("El numero no corresponde! El numero que ingresaste es mayor.")
    elif (menor):
        print("El numero no corresponde! El numero que ingresaste es menor.")

print("El juego ha concluido")

