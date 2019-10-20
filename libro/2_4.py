sue= float(input("Escriba el sueldo del trabajador"))
if sue < 1000:
    nsue= sue * .15 + sue
if sue > 1000:
    nsue= sue * .12 + sue

print(f" Su sueldo actual es de: ${nsue}")

