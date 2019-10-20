sue=int(input("Escribe el sueldo del trabajador :"))
cate=int(input("Escribe la categoria del trabajador :"))
he=int(input("Escribe la horas extras que trabajo :"))
if cate == 1:
    phe = 30
if cate == 2:
    phe = 38
if cate == 3:
    phe = 50
if cate == 4:
    phe = 70
if cate > 4:
        phe = 0
if he > 30:
    nsue=sue+30*phe
else:
    nsue=sue+he*phe
print(f"El nuevo sueldo es {nsue}")
print("Fin del programa")
