#Escribe un programa que solicite al usuario dos números enteros positivos y luego imprima todos los 
# números entre ellos (inclusive) utilizando un bucle while.

numero=int(input("Ingresa el primer numero: "))
numero2=int(input("Ingresa el segundo numero: "))
if numero>numero2:
    i=numero2
    while i<=numero:
        print(i)
        i+=1
elif numero2>numero:
    i=numero
    while i<=numero2:
        print(i)
        i+=1