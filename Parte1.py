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

# Ruta del archivo CSV
with open('datos.csv') as File:
    reader = csv.reader(File, delimiter=',', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)
    data = []  # Lista para almacenar los datos

    for row in reader:
        data += row  # Concatenar la fila actual a la lista 'data'

datos = [int(item) for item in data]  # Convertir los datos a tipo entero

# Ordenar el arreglo
data = sorted(datos)

# Imprimir el arreglo ordenado
print(data)

# Calcular la longitud del arreglo
longitud = len(data)
print(f"N(# total de datos): {longitud}")

media=sum(data)/longitud

print(f"Media: {media}\n")

# Calcular la mediana
if longitud % 2 == 1:
    # Longitud impar
    mediana = data[(longitud - 1) // 2]
else:
    # Longitud par
    mediana = (data[(longitud - 1) // 2] + data[longitud // 2]) / 2

print(f"Mediana: {mediana}\n")

# Calcular la varianza
diferencias_cuadrado = sum([(x - media) ** 2 for x in datos])
varianza = (diferencias_cuadrado)/(longitud-1)

# Calcular la desviación estándar
desviacion_estandar = math.sqrt(varianza)

print(f"Varianza: {varianza}\n")
print(f"Desviación Estándar: {desviacion_estandar}\n")

# Calculo de los cuartiles
print('Calculo de los cuartiles')
if longitud%2==0:
    for k in range(1,4):
        calc_cuart=(k*(longitud)/4)
        cuartil=math.ceil(calc_cuart)
        print(f"Cuartil {k}={cuartil}")
else:
    for k in range(1,4):
        calc_cuart=(k*(longitud)/4)
        cuartil=math.ceil(calc_cuart)
        print(f"Cuartil {k}={cuartil}")


"""
PARTE 2: DIAGRAMA DE TALLO Y HOJA
"""
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
