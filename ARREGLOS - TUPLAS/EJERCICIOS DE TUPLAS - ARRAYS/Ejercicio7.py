

tupla = (" ", "hola", " ", " " , "mundo")
print (tupla)
lista_sin_espacios = list(tupla)

while " " in lista_sin_espacios:
    lista_sin_espacios.remove(" ")
    

tupla1 = tuple(lista_sin_espacios)
print (f"Tupla original: {tupla}")
print (f"Tupla sin espacios: {tupla1}")