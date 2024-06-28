

valor1 = (input("Ingrese una frase: "))
valor2 = (input("Ingrese otra frase: "))
lista = list(valor1) 
lista2 = list(valor2)

numero_lista = len(valor1)

for letra1, letra2 in zip (lista,lista2):
    if (letra1==letra2):
           print(f"Tiene letra similar: {letra2}")