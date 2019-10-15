a= float(input("Introduzca a (no puede ser 0)"))
b= float(input("Introduzca b"))
c= float(input("Introduzca c"))
dis= b**2-4*a*c
x1= ((-b) + dis**0.5) / 2*a
x2= ((-b) - dis**0.5) / 2*a

if dis >=0:
    print(f" Raices Reales X1= {x1}     X2= {x2}")
if dis < 0:
    print(f"No se puede calcular")
print("Fin del programa")

