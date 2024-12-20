#Escribe un programa que solicite al usuario dos números enteros positivos y luego imprima la 
# suma de todos los números entre ellos (inclusive) utilizando un bucle while.

numero1=int(input("Ingrese el primer numero: "))
numero2=int(input("Ingresa el segundo numero: "))
x,y = numero1,numero2
suma=0
if numero1==numero2:
    print(suma)
if numero1>numero2:
    while numero2<=numero1:
        suma+=numero2
        numero2+=1
    print(f"La suma de los numeros entre {y} y {x} es: {suma}")
elif numero2>numero1:
    while numero1<=numero2:
        suma+=numero1
        numero1+=1
    print(f"La suma de los numeros entre {x} y {y} es: {suma}")
