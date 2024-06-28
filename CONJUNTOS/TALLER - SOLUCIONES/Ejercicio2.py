
dic = {"Platano":2350,"Manzana":3800,"Pera":4850,"Naranja":2700}


fruta = str(input("Ingrese una fruta para validar: "))

if fruta in dic:
    kilosFruta = int(input("Ingrese el número de kilos que necesita: "))
    kilos = kilosFruta*dic[fruta]
    print(f"La fruta es {fruta} y el número de kilos {kilosFruta}")
    print(f"-------- Te costará $ {kilos} --------")
else:
    print("La fruta que ingresaste es desconocida en nuestro  inventario.")