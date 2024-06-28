#Colecciones:

notas = [3,4,6,2,6,8,4,9]
print (len(notas))
print (max(notas))
print (min(notas))

print (notas)

print (notas)

res = notas[-3] + notas[5]
print (res)


lista = [1,2,3]
x = lista[2]
print(f"El valor de x: {x}")

print (lista)

lista.insert(2, "Visual Basic")
print (lista)


lenguajes = ["Python", "C++", "Java"]
lenguajes.append("Vscode")
lenguajes.insert(3,"C")
print(lenguajes)


lenguajes.insert(round(len(lenguajes)/2),"Delphi")
print (lenguajes)

print ("Vscode" in lenguajes)


for x in lenguajes:
	print (x, end=",")
        if x == len(lenguajes):
            print (".")
            break
        