#Tipado dinamico, se muestra con el type que tipo de dato es
X=15
print("Tipo de dato de X: ", type (X))
Y = 2
print("Tipo de dato de Y: ", type (Y))
Z = X/Y
print("Tipo de dato de Z: ", type (Z))

#Tipo de dato
X = "Hola"
print(X)
print (type (X))

# Comparadores: Mayores u menores, palabras en listas o tipo de dato
print (3<4)
print ("extraño" in [4,5,12,"extraño"]) #Es la misma palabra en una lista determinada.
print(type("causal") is type("causal")) #Tipo de dato, causal es int y la otra también.


#Pide un número a la persona de tipo entero / Intento de suma
number1 = int(input("numero: "))
number2 = int(input("numero: "))

x=(number1,number2)
print (sum(x))


#Es para llevar siempre mayuscula en la primera letra.
x="hola"
print (x.capitalize()) #Muestra Hola.

#Muestra una parte de la palabra python -> Depende del número y posición requerida.
cad = "python"
print (cad[0]) #Aparece la letra: P

#Forma de separar una frase, le da un espacio de línea
cad2 = "\n escucha hermano \n del que esperala alegrías"
print (cad2)

#Concatenación y formato de cadenas
print ("2)"," hola"+"hey") #El + es forma de juntar las palabras
                           #La coma le da un espacio. 



#Se puede declarar dos variables directamente en el mismo espacio.
lenguaje,version = "python",2
print (f"5) hola mundo {lenguaje} {version}")


cadena = "lenguaje de programación python"
print (cadena[:3]) #len
print (cadena[15:]) #La cadena empieza después de contar 15, cuenta de 16 para adenlante "gramación python"
print (cadena[-6:]) #desde que los dos puntos estén adelante, empieza al revés (desde la parte de atrás). NO CUENTA EL CERO.
    


#Cambiar el tipo de dato
#String es letra, y int es entero (número)
a, b = 5, 4

print (a+b) #35 en letra.
print (int(a),int(b))#3 5 pero en entero, número.
print (int(a)+int(b), type(a), type(b))

print (type(a))
print (a+b, "este espacio quedó convertido en int")
print (type(a))


#Convierte a mayusculas:
cadena = "mi pobre angelito"
cad1 = cadena.upper() #TIENE QUE GUARDARSE EN UNA VARIABLE
print (cad1)

#Devuelve el número de veces que se encuentra una letra en subcadena"
cad2 = cadena.count("o")
print (cad2)

print (f"la letra está {cad2} en la frase {cad1}")
#La F toma las variables en parentesis.
# Y hay que poner sí o sí {}

cad3 = cadena.replace("mi pobre","dulce, pobrecito") #Reemplaza una subcadena por otra en la cadena original.
print (cad3) #En la izquierda se pone la parte que se quiere reemplazar del texto, y en la derecha el texto que quieres poner.


#Lectura de datos ingresada por el usuario
marca = input("hola, ingresa una marca: ")
print (marca)

# f significa que toma variables en el parentesis
precio = int(input("decí un precio: "))
print (f"El auto marca {marca}, tiene un precio de ${precio}, y tiene un descuento de {precio*.9}")

#El format significa que le ingresa las variables después, pero es mejor la primera
print("El auto marca {} tiene precio de {:,}, y tiene un descuento de {:,}".format(marca,precio,precio*0.9))


#El input siempre toma como string.



























