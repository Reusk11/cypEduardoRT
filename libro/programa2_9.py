prebas=float(input("precio:$"))
if prebas > 500:
    IMP=20*0.30+(prebas-40)*0.50
elif prebas > 40:
    IMP=20*0.30+(prebas-40)*0.40
elif prebas > 20:
    IMP= (prebas-20)*0.30
else:
    IMP=0
preto= prebas + IMP
print(f"El precio del objeto es de:${prebas} y con impuesto su valor es ${preto}")
print("Fin del programa")
