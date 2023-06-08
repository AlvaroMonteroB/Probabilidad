import lib




path="datos.csv"
filas,columnas,datos=lib.read_csv(path)
listas=lib.get_cols(datos)
matriz=lib.matriz_co(listas)
lib.print_matriz(matriz)
