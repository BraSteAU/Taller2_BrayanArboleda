#Escribe un programa que solicite al usuario un número entero positivo y luego imprima los primeros 
# n números impares utilizando un bucle while.

numero=int(input("Ingresa un numero: "))
i=1
while i<=numero:
    if i%2!=0:
        print(i)
    i+=1