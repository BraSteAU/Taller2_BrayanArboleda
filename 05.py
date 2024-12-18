numero=int(input("Ingresa un numero: "))
i=2
while i<numero:
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)
    i+=1



