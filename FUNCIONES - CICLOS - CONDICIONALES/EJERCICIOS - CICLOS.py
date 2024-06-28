# #Ejercicio 1


n = int(input("Ingresa un número entero positivo: "))

for n in range (1, n+1, 2):
        print(f"{n}",end=",")


# #Ejercicio 2


password = str(input("Ingresa una NUEVA contraseña para tu cuenta: "))
print ("Tu contraseña ha sido creada exitosamente")
nueva = str(input("Ingresa la contraseña creada para ingresar otra vez: "))


while password != nueva:
        nueva = str(input("Ingresa la contraseña creada para ingresar otra vez: "))
        if (nueva == password ):
                print (f"Es correcta, tu contraseña es {password}")
        else:
                print ("Incorrecta")
                


# #Ejercicio 3

numero = int(input("Ingrese un número para mostrarlo en la tabla de multiplicar: "))
x = 1
for x in range (1, 11):
        print(f"{numero} x {x} = ", numero*x)  
        
#Ejercicio 4

acum = 0 
contador = 0
contadorimpar = 0
contadorpar = 0
numgrande= 100
numerito = 0
numeromenor = 0

while True:
        numero = int(input("Ingrese un número: "))
        
        if numero>0:
                acum = acum + numero
                
        
        if numero%2==1 and numero>0:
                contadorimpar = contadorimpar + 1
                
        if numero%2==0 and numero>0:
                contadorpar = contadorpar + 1 
        
        if numero>numeromenor and numero>=1:
                numerito = numero 
                        
        if numero<numgrande and numero>=0:
                numeromenor = numero
                pass
        
        if numero<0:
                print (f"La sumatoria es {acum}")
                print (f"Hay {contadorimpar} números impares")
                print (f"Hay {contadorpar} números pares")
                print (f"El número mayor es {numerito}, y el número es menor {numeromenor}")
                break
                
                
        

     
# #Ejercicio 5


personas = int(input("¿Cuántas personas ingresaron al partido?: "))
estrato = int(input("¿Cuál es tu estrato?: "))
edad = int(input("¿Cuál es tu edad?: "))
boleta = int(input("Valor de la boleta: "))
descontado = ""
recaudado = personas*boleta
total = ""

if estrato==1 and edad<18:
        descontado = recaudado*0.2
        total = recaudado-descontado
print(f"Lo recaudado fue {recaudado}, y el descontado es {descontado} \npara {personas} que ingresaron al partido")
print (f"Total en dinero es {total}")
        
        
if estrato==1 and edad>=18:
        descontado = recaudado*0.15
        total = recaudado-descontado
        print(f"Lo recaudado fue {recaudado}, y el descontado es {descontado} \npara {personas} que ingresaron al partido")
        print (f"Total en dinero es {total}")

if estrato==2 and edad<18:
        descontado = recaudado*0.1 
        total = recaudado-descontado
        print (f"Total en dinero es {total}")

if estrato==2 and edad>=18:
        descontado = recaudado*0.05
        total = recaudado-descontado
        print(f"Lo recaudado fue {recaudado}, y el descontado es {descontado} \npara {personas} que ingresaron al partido")
        print (f"Total en dinero es {total}")



   
# #Ejercicio 6

# contrasena = (input("Ingrese una contraseña: "))
# print("Lista tu contraseña")

# entrada = ""

# for x in range (1,6,):
#         entrada = (input("Ingrese una contraseña: "))
        
#         if contrasena!=entrada: 
#                 print("Contraseña incorrecta")        
                
#         if contrasena==entrada:
#                 print("Bienvenido")
#                 break
