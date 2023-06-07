import lib




path="datos.csv"
filas,columnas,datos=lib.read_csv(path)
columnas=lib.get_cols(datos)
matriz=lib.matriz_co(columnas)
lib.print_matriz(matriz)
