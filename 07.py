#Escribe un programa que solicite al usuario un número entero positivo y luego imprima la suma de los 
# primeros n números pares utilizando un bucle while.
numero=int(input("Ingresa un numero: "))
i=2
suma=0
while i<=numero:
    if i%2==0:
        suma+=i
    i+=1
print(f"La suma de los numeros pares hasta {numero} es: {suma}")