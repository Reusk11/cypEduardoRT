a = int(input("introduce un entero positivo:"))
b = int(input("introduce un entero positivo:"))
c = int(input("introduce un entero positivo:"))
if a>b :
    if a > c :
        print(f" a es el mayor y su valor es {a}")
    elif a == c:
        print(f" a y c son iguales a {a} y son los de mayor valor")
    else:
        print(f"c que vale {c} es el mayor")
elif a == b:
    if a>c:
        print(f" a y b son de mayor valor a {a}")
    else:
        print(f"a b y c son iguales a {a}")
        print(f" c que vale {c} es el mayor")
elif b > c:
    print(f" b que vale {b} es el mayor")
elif  b == c:
    print(f" b y c son los mayores valores {c}")
else: print(f" c que vale {c} es el mayor")
print("fin del programa:)")

