
#CONDICIONALES
#EJERCICIO 1

motor = input("El motor está encendido o apagado? (s,n) ")
tempmotor = int(input("¿Qué temperatura tiene el motor? "))

if motor=="s" and tempmotor>=80:
    print ("El motor se ha apagado por seguridad ")


elif motor=="n":
    print ("Está apagado")

elif motor=="s" and tempmotor<80:
    print ("El motor está prendido pero está bien de temperatura")


#EJERCICIO 2

velocidadescarga = 10
velocidad2 = 5
velocidad3 = 1
conexion = int(input("¿Cuál es su conexión de internet? "))
archivo = int(input("¿Qué tamaño es el archivo para descargar?"))
tiempo = (archivo/conexion)

if conexion>20:
    print(f"Su velocidad de descarga es de {velocidadescarga}mbps \ny el tiempo para descargar su archivo es de {tiempo}")

elif conexion<20 and conexion>5:
    print(f"Su velocidad de descarga es de {velocidad2}mbps, \ny el tiempo para descargar su archivo es de {tiempo}")

elif conexion<5:
    print(f"Su velocidad de descarga es de {velocidad3}mbps, \ny el tiempo para descargar su archivo es de {tiempo}")


#EJERCICIO 3

estrato = int(input("¿Qué estrato eres? "))
edad = int(input("¿Cuántos años tienes? "))
matricula = float(input("¿Cuánto pagas por matricula? "))
descuentos = (matricula*0.20)
des1 = (matricula-descuentos)
descuentos2 = (matricula*0.15)
des2 = (matricula-descuentos2)
descuentos3 = (matricula*0.1)
des3 = (matricula-descuentos3)
descuentos4 = (matricula*0.05)
des4 = (matricula-descuentos4)

if estrato==1 and edad<18:
           print(f"El valor a pagar será {des1}, y el valor del descuento ha sido {descuentos}")

elif estrato==1 and edad>=18:
    print(f"El valor a pagar será {des2} , y el valor del descuento ha sido {descuentos2}")

elif estrato==2 and edad<18:
     print(f"El valor a pagar será {des3} , y el valor del descuento ha sido {descuentos3}")

elif estrato==2 and edad>=18:
     print(f"El valor a pagar será {des4} , y el valor del descuento ha sido {descuentos4}")
    

#EJERCICIO 4
nombre = input("Ingrese su nombre completo: ")
edad = int(input("Ingrese su edad: "))

if edad>17:
    print(f"{nombre}, usted debe tener su número de afiliación.")
else:
    print(f"{nombre}, usted no debe tener su número de afiliación.")
    

#EJERCICIO 5
num1, num2, num3 = int(input("Ingrese un número: ")) , int(input("Ingrese un número: ")) , int(input("Ingrese un número: "))

if num1>num2 and num1>num3:
    print (f"{num1} es mayor que {num2}, {num3}")

elif num2>num1 and num2>num3:
    print (f"{num2} es mayor que {num1}, {num3}")
    
elif num3>num1 and num3>num2:
    print (f"{num3} es mayor que {num1}, {num2}")
