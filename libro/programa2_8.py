com=float(input("precio de lo comprado: $"))
if com < 500:
    print(f"TOTAL A PAGAR{com}")
elif com<= 1000:
    pag=com-(com*0.05)
    print(f"TOTAL A PAGAR :${pag}")
elif com<= 7000:
    pag=com-(com*0.11)
    print(f"TOTAL A PAGAR :${pag}")
elif com<= 15000:
    pag=com-(com*0.18)
    print(f"TOTAL A PAGAR :${pag}")
else:
    pag=com-(com*0.25)
    print(f"TOTAL A PAGAR :${pag}")
print("Fin del programa")
