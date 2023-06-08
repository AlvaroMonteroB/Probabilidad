import csv



def read_csv(path):
    with open(path,"r") as file:
        archivo=list(csv.reader(file))
        file.close
    for renglon in archivo:
        for i in range(len(renglon)):
            renglon[i]=float(renglon[i])
    #print(str(len(archivo))+str(len(archivo[0])))
    return len(archivo),len(archivo[0]), archivo    #filas, columnas y csv
     #Vamos a retornar una tupla con el largo y ancho del csv

def get_cols(archivo):#Pasar de el formato csv a que cada hilera esté en una lista
    columnas=list()
    for i in range(len(archivo[0])):#Nos movemos en las columnas
        auxcol=list()
        for j in range(len(archivo)):#Nos movemos en las filas
            auxcol.append(archivo[j][i])
        columnas.append(auxcol)
        auxcol=None
    return columnas

    

def matriz_co(columnas):
    matriz=list()
    for i in range(len(columnas)):
        renglon=list()
        for j in range(len(columnas)):
            renglon.append(round(covarianza(columnas[i], columnas[j]),2))
        matriz.append(renglon)
    return matriz





def covarianza(x:list,y:list):
    xprom=sum(x)/len(x)
    yprom=sum(y)/len(y)
    covxy=0
    for i in range(0,len(x),1):
        covxy+=((x[i]-xprom)*(y[i]-yprom))/len(x)
    return covxy
    

def print_matriz(matriz):
    tam=len(matriz)
    for renglon in matriz:
        for col in renglon:
            print(str(col)+" ",end="")
        print("\n")
   