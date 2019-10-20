cla=int(input("Dame la clave regional :"))
numin=int(input("Cuantos minutos duro la llamada :"))
if cla==12:
    cos=numin*2
if cla==15:
    cos=numin*2.2
if cla==18:
    cos=numin*4.5
if cla==19:
    cos=numin*3.5
if cla==23:
    cos=numin*6
if cla==25:
    cos=numin*6
if cla==29:
    cos=numin*5
print(f"El costo de la llamada fue ${cos}")
print("Fin del programa")
