mat= float(input("Introduzca la matrícula del alumno"))
cal1= float(input("Introduzca la calificacion del alumno"))
cal2= float(input("Introduzca la calificacion del alumno")) 
cal3= float(input("Introduzca la calificacion del alumno")) 
cal4= float(input("Introduzca la calificacion del alumno"))
cal5= float(input("Introduzca la calificacion del alumno"))
pro = (cal1 + cal2 + cal3 + cal4 + cal5) / 5
if pro >=6:
    print(f" {mat} {pro} APROBADO")
if pro <6:
    print(f"{mat} {pro} REPROBADO")
print("Fin del programa")
