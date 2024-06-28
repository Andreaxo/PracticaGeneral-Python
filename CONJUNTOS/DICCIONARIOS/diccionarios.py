#Diccionario



diccionario = {2,4,5,6,7,89}

print(type(diccionario))

diccionario = {"tres":"three","dos":"dos","cinco":"five"}
print(diccionario)
print(type(diccionario))
print(diccionario["tres"])


dic = {"llave1":"a",2:[2,34,5],4:"C",5:8}

print(type(dic))
print(dic)
print(dic["llave1"])
print(dic[2][1]) # Sólo se recorre porque este es una lista


capitales = {"caldas":"manizales","risaralda":"pereira","valle":"cali"}
print(capitales)
print(f"La capital de Caldas es {capitales['caldas']}")
capitales["Armenia"]="Quindio"

capitales = {"Caldas":"Manizales","Risaralda":"Pereira","Valle":"Cali"}
print(capitales)
capitales["Valle"] = "Santiago de cali" #Se puede actualizar con alguna clave
print(capitales) 
del(capitales ["Valle"])
print(capitales)

alumnos = {"juan":[23,"calle 10",323],"luis":[45,"carrera 12"]}
print(alumnos)
print(alumnos["luis"][0])


edades = {'Hector':27,'Juan':45,'Maria':34}
print(edades)
print(f"{'Hector'} tiene {edades['Hector']} años")
    

for item in edades.items():
    print(item)
    
    
for p, q in edades.items():
    print(p, '-' ,q)


for item in edades.keys():
    print(item)
    
    
for item in edades.values():
    print(item)
    

