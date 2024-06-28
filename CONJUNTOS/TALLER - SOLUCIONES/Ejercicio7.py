contador = 0
dic = {}


print ("------------ Bienvenido al supermercado --------------")
numero = int(input("Ingrese ¿Cuántos productos quieres ingresar?: "))

for x in range (numero):
    producto = str(input("Ingrese un producto: "))
    precio = dic[producto] = int(input("Ingrese un valor: "))

print ("\n \n Lista de compra")
print ("-------------------")
for clave in dic:
    print(f" {clave} -- Precio: {dic[clave]}")
    
for producto in dic.values():
    contador = producto+contador


print(f" Total =      {contador}")