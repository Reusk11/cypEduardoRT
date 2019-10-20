enf=int(input("Que tipo de enfermadad es :"))
edad=int(input("Edad del enfermo :"))
dias=int(input("Dias que tiene enfermo :"))
if enf==1:
    COSTOT=dias*25
elif enf==2:
    COSTOT=dias*16
elif enf==3:
    COSTOT=dias*20
elif enf==4:
    COSTOT=dias*32
if edad >= 14 and edad<=22:
    COSTOT=COSTOT*1.10
print(f"EL costo total es de ${COSTOT}")
print("Fin del programa")
