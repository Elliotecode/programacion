import math
lista_datos = [] #nada
tabla_frecuencia = [] #nada
datos_otorgados = 0 #nada

#entrada
numero_de_datos = int(input("Ingrese el número de datos: ")) #sacar el numero maximo de datos a preguntar
while datos_otorgados < numero_de_datos:
    lista_datos.append(int(input("ingrese los datos:  "))) # añadir los datos
    datos_otorgados += 1

#proceso

#datos necesarios

#organizar los datos
lista_datos_ordenada = sorted(lista_datos)
#sacar el rango
num_menor = (lista_datos_ordenada[0])
num_mayor = (lista_datos_ordenada[numero_de_datos - 1])
rango = num_mayor - num_menor
#numero de intervalos
numero_intervalos = 1+3.322*math.log10(numero_de_datos)
numero_intervalos_redo = round(numero_intervalos)
#amplitud de intervalos
amplitud_intervalos = rango/numero_intervalos_redo

#tabla de frecuencia

#salida
print("\n\ndatos otorgados:")
print("lista de datos: ", lista_datos_ordenada)
print("numero de datos: ", numero_de_datos)

print("\ndatos procesados:")
print("dato menor: ", num_menor, "    dato mayor: ", num_mayor)
print("rango: ", rango)
print("numero de intervalos: ≈ ", numero_intervalos_redo, "    amplitud de intervalos: ≈ ", amplitud_intervalos)
