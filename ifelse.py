edad= int(input("Dame tu edad"))
ine= bool( int( input("Tienes INE? (0 no / 1 si)")))
if edad >= 18 and ine == True:
    print("Es mayor de edad")
    print("Puede entrar al bar")
else:
    print("Eres menor de edad")
    print("Ve a jugar CALABAZA")
print("fin del programa")
