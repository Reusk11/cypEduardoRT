l1= int(input("Escriba la medida del lado 1"))
l2= int(input("Escriba la medida del lado 2"))
l3= int(input("Escriba la medida del lado 3"))
s= (l1 + l2 + l3)/2
area= (s * (s - l1) * (s - l2) * (s - l3))**0.5
print(f"El area del triángulo es: {area}")
