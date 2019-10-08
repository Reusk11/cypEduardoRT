cate= int(input("Introduzca la categoría del trabajador: 1-4"))
sue= float(input("Introduzca el sueldo del trabajador"))
nsue= 0
if cate ==1:
    nsue= sue * 1.15
elif cate ==2:
    nsue= sue *1.10
elif cate ==3:
    nsue= sue *1.08
elif cate ==4:
    nsue= sue *1.07
print(f"La categoria es {cate} y su nuevo sueldo es: {nsue}")
print("fin del programa")
