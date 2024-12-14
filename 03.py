#Escribe un programa que solicite al usuario un número entero positivo y luego calcule la suma de 
# todos los números divisibles por 3 desde 1 hasta ese número utilizando un bucle while.

numero=int(input("Ingresa un numero: "))
i=1
suma=0
while i<=numero:
    if i%3==0:
        suma+=i
    i+=1
print(f"La suma de todos los numeros divisibles por 3 desde 1 hasta {numero} es: {suma}")