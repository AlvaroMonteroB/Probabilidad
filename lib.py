import csv



def read_csv(path):
    with open(path,"r") as file:
        archivo=list(csv.reader(file))
        file.close
    for renglon in archivo:
        for columna in renglon:
            columna=float(columna)
    return len(archivo),len(archivo[0]), archivo    #filas, columnas y csv
     #Vamos a retornar una tupla con el largo y ancho del csv

def get_cols(archivo,num_cols):
    columnas=list()
    for j in enumerate(archivo):
        auxcol=list()
        for i in enumerate(archivo[0]):
            auxcol.append(archivo[i][j])
        columnas.append(auxcol)
        auxcol=None
    return columnas

    

#Dimensiones de la matriz, no de los datos
def matriz_co(columnas):
    matriz=list()
    for i in range(len(columnas)):
        renglon=list()
        for j in range(len(columnas)):
            renglon.append(covarianza(columnas[i], columnas[j]))
        matriz.append(renglon)
    return matriz





def covarianza(x:list,y:list):
    xprom=sum(x)/len(x)
    yprom=sum(y)/len(y)
    covxy=0
    for i in range(0,len(x),1):
        covxy+=((x[i]-xprom)(y[i]-yprom))/len(x)
    return covxy
    