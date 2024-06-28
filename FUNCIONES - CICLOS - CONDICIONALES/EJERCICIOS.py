
#EJERCICIO 1.

cantidad_frutos_recolectados = int(input("Ingrese los frutos recolectados: "))
cantidad_frutos_producidos = int(input("Ingrese los frutos producidos: "))

indice_cosecha = (cantidad_frutos_recolectados/cantidad_frutos_producidos)*100

total = (f"La cantidad relacionada con el  indice de cosecha es: {indice_cosecha}")
print (total)


#EJERCICIO 2

nota1, nota2, nota3 = float(input("Tu nota: ")), float(input("Tu nota: ")) , float(input("Tu nota: "))
print (f"Su nota n° 1 fue: {nota1} \nSu nota n°2 fue: {nota2} \nSu nota n°3 fue: {nota3}")
calificación_examen = float(input("¿Cuál fue tu calificación del examen? "))
calificación_trabajo_final = float(input("Nota del trabajo final: "))

promedionotas = (nota1+nota2+nota3)/3
print (promedionotas)


print (promedionotas*0.55+calificación_examen*0.3+calificación_trabajo_final*0.15)


#EJERCICIO 3

velocidad, tiempo = float(input("Ingrese una velocidad: ")), float(input("Ingrese un tiempo: "))
distancia = (velocidad*tiempo)
print (f"La distancia recorrida por un automovil que tiene {velocidad}m/s durante {tiempo} es: {distancia}")

                                 

#EJERCICIO 4

nombre = input("Ingrese su nombre: ")

respuestacorrecta =  int(input("¿Cuántas respuestas correctas tuvo? "))
respuestaincorrecta = int(input("¿Cuántas respuestas incorrectas tuvo? "))
respuestablanco =  int(input("¿Cuantas respuestas en blanco tuvo? "))

respuestacorrecta2 = (respuestacorrecta*4)

respuestablanco = (respuestablanco*0)

puntajetotal = (respuestacorrecta2-respuestaincorrecta)
print (nombre)
print (puntajetotal)

#EJERCICIO 5

nombreequipo = input("Ingrese el nombre del equipo: ")
partidosganados = int(input("¿Cuántos partidos ganados tuvo? "))
partidosperdidos = int(input("¿Cuántos partidos perdidos tuvo? "))
partidosempatados = int(input("¿Cuántos partidos empatados tuvo? "))

partidoG = (partidosganados*3)
puntajetotal = (partidoG+partidosempatados)
print (f"El equipo {nombreequipo} tiene los siguientes puntos: {puntajetotal}")


#EJERCICIO 6.
frase = input("Ingrese alguna frase: ")
frase2 = (frase.split())
print (frase2)
frase3 = len(frase2)
print (f"La frase tiene {frase3} palabras")
