
dic = {'Matemáticas': 6, 'Física': 4, 'Química': 5}

for p, q in dic.items():
    print (f"La asignatura es {p} y el crédito correspondiente es {q}")
    print ("---------------------------------------------------------")


print("----------- Tus créditos ---------------")
credito1 = int(input(f"Ingrese el credito de Matemáticas: "))
credito2 = int(input(f"Ingrese el credito de Física: "))
credito3 = int(input(f"Ingrese el credito de Química: "))

dic['Matemáticas'] = credito1
dic['Física'] = credito2
dic['Química'] = credito3

suma = 0
for p, q in dic.items():
    print(f"La asignatura es {p} y tus créditos son {q}")
    suma = q+suma
    print(f"La suma total de los créditos es: {suma} ")