#Escribe un programa que solicite al usuario un número entero positivo y luego imprima todos los 
# números entre 1 y ese número en orden inverso utilizando un bucle while.

numero=int(input("Ingresa un numero: "))
i=numero
while numero>0:
    print(numero)
    numero-=1
print("💥")