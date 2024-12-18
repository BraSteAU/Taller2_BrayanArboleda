#Escribe un programa que solicite al usuario un número entero positivo y luego imprima la suma de los 
# cuadrados de todos los números desde 1 hasta ese número utilizando un bucle while.

numero=int(input("Ingresa un numero: "))
i=1
suma=0
while i<=numero:
    suma+=i*i
    i+=1
print(f"La suma de los cuadrados de 1 hasta {numero} es: {suma}")