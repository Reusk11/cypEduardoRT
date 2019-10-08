a= int(input("Dame un numero entero positivo"))
b= int(input("Dame un numero entero positivo"))
c= int(input("Dame un numero entero positivo"))
if  a>b :
    if a>c :
        if b>c:
            print(F"{a} > {b} > {c}")
        else:
            print(F"{a} > {c} > {b}")
    else:
        print(F"{c} > {a} > {b}")
else:
    if b>c:
        if a>c:
            print(F"{b} > {a} > {c}")
        else:
            print(F"{b} > {c} > {a}")
    else:
        print(F"{c} > {b} > {a}")
print("Fin del programa")




