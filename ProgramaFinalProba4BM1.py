import lib

import csv
import math
import statistics as st

def stem_and_leaf(data):
    # Se ordena la lista de datos de forma ascendente
    sorted_data = sorted(data)
    
    # Se inicializan las listas para los tallos y las hojas
    stems = []
    leafs = []

    # Se recorre cada número en la lista ordenada
    for num in sorted_data:
        # Se calcula el tallo dividiendo el número entre 10 (parte entera de la división)
        stem = num // 10
        
        # Se calcula la hoja tomando el residuo de la división entre 10
        leaf = num % 10

        # Se añade el tallo a la lista de tallos
        stems.append(stem)
        
        # Se añade la hoja a la lista de hojas
        leafs.append(leaf)

    # Se retornan las listas de tallos y hojas
    return stems, leafs

print("==================================================================================================")

# Ruta del archivo CSV
with open('datos2.csv') as File:
    reader = csv.reader(File, delimiter=',', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)
    data = []  # Lista para almacenar los datos

    for row in reader:
        data += row  # Concatenar la fila actual a la lista 'data'

datos = [int(item) for item in data]  # Convertir los datos a tipo entero


"""
data = []

# Ruta del archivo de texto
archivo = 'datos.txt'

with open(archivo, 'r') as file:
    for line in file:
        line = line.strip()  # Eliminar espacios en blanco al inicio y final de la línea
        if line:  # Ignorar líneas vacías
            elementos = line.split()  # Dividir la línea en elementos individuales
            data.extend(elementos)  # Agregar los elementos a la lista 'data'

datos = [int(item) for item in data]
"""
"""
datos = []

# Ruta del archivo de texto
archivo = 'datos2.txt'

# Lectura del archivo de texto
with open(archivo, 'r') as file:
    # Iterar sobre cada línea del archivo
    for line in file:
        # Eliminar los caracteres de salto de línea al final de cada línea
        value = line.strip()
        
        # Convertir el valor a entero y agregarlo a la lista de datos
        datos.append(int(value))
"""

# Ordenar el arreglo
data = sorted(datos)

# Imprimir el arreglo ordenado
print(f"Los datos ordenados son: \n{data}")

# Calcular la longitud del arreglo
longitud = len(data)
print(f"\nN(# total de datos): {longitud}")

media=sum(data)/longitud

print(f"\nMedia: {media}\n")

# Calcular la mediana
if longitud % 2 == 1:
    # Longitud impar
    mediana = data[(longitud - 1) // 2]
else:
    # Longitud par
    mediana = (data[(longitud - 1) // 2] + data[longitud // 2]) / 2

print(f"Mediana: {mediana}\n")

# Calcular la moda
moda=st.mode(datos)
print(f"Moda: {moda}\n")

# Calcular la varianza
diferencias_cuadrado = sum([(x - media) ** 2 for x in datos])
varianza = round((diferencias_cuadrado)/(longitud-1),2)

# Calcular la desviación estándar
desviacion_estandar = round(math.sqrt(varianza),2)

print(f"Varianza: {varianza}\n")
print(f"Desviación Estándar: {desviacion_estandar}\n")

print("==================================================================================================")

# Calculo de los cuartiles
print('\nCalculo de los cuartiles')
cuart_1=(1*(longitud+1)/4)
q_uno=math.ceil(cuart_1)
print(f"\nLa posicion del Cuartil 1 = {q_uno}")
print(f"El cuartil 1 es: {datos[q_uno-1]}")

q_dos=mediana
print(f"\nEl cuartil 2 es: {q_dos}")

cuart_3=(3*(longitud+1)/4)
q_tres=math.ceil(cuart_3)
print(f"\nLa posicion del Cuartil 3 = {q_tres}")
print(f"El cuartil 3 es: {datos[q_tres-1]}")

print("\n==================================================================================================")

rango_intercuartil=datos[q_tres-1]-datos[q_uno-1]
print(f"\nRango intercuartil = {rango_intercuartil}")

atipicos_inferiores=datos[q_uno]-1.5*rango_intercuartil
print(f"Valor atipico leve inferior = {atipicos_inferiores}")

atipicos_superiores=datos[q_tres]+1.5*rango_intercuartil
print(f"Valor atipico leve superior = {atipicos_superiores}")

atipicos_ext_inferiores=datos[q_uno]-3*rango_intercuartil
print(f"Valor atipico extremo inferior = {atipicos_ext_inferiores}")

atipicos_ext_superiores=datos[q_tres]+3*rango_intercuartil
print(f"Valor atipico extremo superior = {atipicos_ext_superiores}")

puntos_atipicos_inf = []
puntos_atipicos_sup = []
puntos_atipicos_inf_ex = []
puntos_atipicos_sup_ex = []

for numero in data:
    if numero < atipicos_inferiores :
        puntos_atipicos_inf.append(numero)

for indice in data:
    if indice > atipicos_superiores :
        puntos_atipicos_sup.append(indice)

print(f"\nLos puntos atipicos inferiores son: {puntos_atipicos_inf}")
print(f"Los puntos atipicos superiores son: {puntos_atipicos_sup}")

for num in data:
    if num < atipicos_ext_inferiores:
        puntos_atipicos_inf_ex.append(num)

for index in data:
    if index > atipicos_ext_superiores :
        puntos_atipicos_sup_ex.append(index)

print(f"\nLos puntos atipicos inferiores extremos son: {puntos_atipicos_inf_ex}")
print(f"Los puntos atipicos superiores extremos son: {puntos_atipicos_sup_ex}")


"""
PARTE 2: DIAGRAMA DE TALLO Y HOJA
"""
print("==================================================================================================")

print("\nDIAGRAMA DE TALLOS Y HOJA\n")

# Se llama a la función stem_and_leaf con los datos de ejemplo y se obtienen las listas de tallos y hojas
stems, leafs = stem_and_leaf(data)

# Se crea un diccionario para almacenar las hojas correspondientes a cada tallo
stem_leaf_dict = {}

# Se itera sobre los índices de los tallos
for i in range(len(stems)):
    # Si el tallo no está presente en el diccionario, se crea una nueva clave con la hoja correspondiente
    if stems[i] not in stem_leaf_dict:
        stem_leaf_dict[stems[i]] = [leafs[i]]
    # Si el tallo ya está presente en el diccionario, se agrega la hoja a la lista existente
    else:
        stem_leaf_dict[stems[i]].append(leafs[i])

# Se itera sobre las claves del diccionario de tallos y hojas, en orden ascendente
for stem in sorted(stem_leaf_dict.keys()):
    # Se imprime cada tallo seguido de las hojas correspondientes (ordenadas)
    print(f"{stem} | {' '.join(map(str, sorted(stem_leaf_dict[stem])))}")

print("\n==================================================================================================")

import csv
import numpy as np

# Rango de valores para agrupar
rango_inicial = 0
rango_final = 100
ancho_rango = 10

# Ruta del archivo CSV
file_path = 'datos.csv'

"""
============= PARTE 3: TABLA DE FRECUENCIAS ===============================
"""
print('\t\tINTERVALOS')
minimo = min(datos)
maximo = max(datos)
rango = maximo - minimo
k_intervalos = 1 + 3.322*math.log10(len(datos))
if(math.floor(k_intervalos) % 2 != 0):  #se recomienda redondear a abajo, pero si es par ese número
    pass                                #-> se redondea a arriba
else:
    k_intervalos = math.ceil(k_intervalos)

print('número de intervalos: ', k_intervalos)
print('rango: ', rango)
amplitud = round(rango / k_intervalos)
print('amplitud: ', amplitud)
intervalos = []
inicio = 0

for i in range(int(k_intervalos) - 1):
    if(i == 0):
        inicio = minimo + amplitud
        intervalo = [minimo, inicio]
        intervalos.append(intervalo)
    inicio = inicio + amplitud
    intervalo = [inicio - amplitud, inicio]
    intervalos.append(intervalo)
    
    
for intervalo in intervalos:
    i = 0
    datos_frecuencia = [dato for dato in datos if dato >= intervalo[0] and dato < intervalo[1]]
    frecuencia = len(datos_frecuencia)
    print('Intervalo: ',intervalo ,'\tFrecuencia: ', frecuencia)

print("\n==================================================================================================\n")

filas,columnas,datos=lib.read_csv(file_path)
listas=lib.get_cols(datos)
matriz=lib.matriz_co(listas)
lib.print_matriz(matriz)
