

print ("_________________ PROGRAMA _______________")
cuentas = int(input("¿Cuántas veces vas a ingresar usuarios?: "))


for x in range (cuentas):
    nombre = str(input("Ingrese un nombre: "))
    edad = int(input("Ingrese una edad: "))
    direccion = str(input("Ingrese su dirección: "))
    telefono = int(input("Ingrese su número de celular: "))
    dic = {nombre:nombre,edad:edad,direccion:direccion,telefono:telefono}
    x += 1
    print("______________________________________________________________")
    print (f"El nombre del usuario {x} es {dic[nombre]}")
    print (f"La edad del usuario {x} es {dic[edad]} ")
    print (f"La dirección del usuario {x} es {dic[direccion]} ")
    print (f"Su número del usuario {x} es {dic[telefono]}")
    print("_____________________________________________________________")