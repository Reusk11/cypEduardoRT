sue= float(input("Cual es el sueldo del trabajador : $ "))
if sue < 1000:
    aum= sue * .15
    nsue= sue + aum
    print(f"Su nuevo sueldo sera ${nsue}")
if sue > 1000:
    print(f" Su sueldo es de: ${sue}")

