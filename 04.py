numero=int(input("Ingresa un numero: "))
suma=0
cantidad=len(str(numero))
i=numero
while(i>0):
    x=i%10
    suma+=x**cantidad
    i//=10
if(suma==numero):
    print(f"El numero {numero} es un numero de Amstrong")
else:
    print(f"El numero {numero} no es un numero de Amstrong")
