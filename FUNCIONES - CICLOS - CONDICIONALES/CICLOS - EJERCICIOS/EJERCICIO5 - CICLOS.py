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

