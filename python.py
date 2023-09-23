maxf=3
maxc=5
a = [[0.0]*maxc for_in range(maxf)]

#Leer el array
for f in range(maxf):
    for c in range(maxc):
        a[f][c]= float(input())

        #Escribir el array
        for f in range(maxf):
            for c in range(maxc):
                print(a[f][c], end="")
                print()