otra = True
suma = 0.0
cont=0
while(otra == True):
    cal= float(input("Calificacion"))
    cont +=1
    suma += cal
    otra = bool(int(input("Hay mas alumnos(0 No, 1 si):")))
print("suma",suma)
print("Promedio", suma/cont)
print("fin del prgrama")
