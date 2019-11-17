import sys
import csv
import sklearn.metrics
import numpy as np
from distantziak import  Distantziak as distance
def newClusterization(model,data,newInstances,results):
    cluster = open(model,'r') #cluster model
    vectores =[]
    with open(data) as trainCsv:
        data = csv.reader(trainCsv, delimiter=',')
        clust = cluster.readlines()
        k = int(clust[0])
        dist = int(clust[1])
        centroid = []
        pertenencias =  []
        j = 0
        while j < k:
            cluster = []
            pertenencias.append(cluster)
            j = j + 1
        distancias ={}
        vectorData = {}
        #cargar centroides
        for cent in range(2,k+2):
            newCentroid = clust[cent][1:-2]
            centroid.append( newCentroid.split(","))
        clusterCentroids = np.array(centroid)
        clusterCentroids = clusterCentroids.astype(np.float64)

        #cargar vectores y ordenarlos
        for lerroa in data:
            vectorData[lerroa[0]] = lerroa[1:]
            vectores.append(lerroa[0])
        for v in vectores:
            z = 0
            distancia = 0

            while z < k:

                distancia2 = distance.calcularDistancia(distance, dist, clusterCentroids[z], vectorData[v])
                distancias[v+str(z)] = distancia2
                if (distancia2 < distancia or distancia == 0):
                    distancia = distancia2
                    c = z
                z = z + 1

            pertenencias[c].append(v)
        newPetenencias = np.array(pertenencias)

    doc = open(results,'a+')  # resultados
    with open(newInstances) as unclustered:
        unclustData = csv.reader(unclustered, delimiter=',')
        for instance in unclustData:
            name = instance[0]
            values = instance[1:]
            clusterNumb =-1
            z = 0
            distancia = 0

            while z < k:
                distancia2 = distance.calcularDistancia(distance, dist, clusterCentroids[z], values)
                if (distancia2 < distancia or distancia == 0):
                    distancia = distancia2
                    clusterNumb = z
                z = z + 1
            neares = []

            if clusterNumb !=-1:
                mindistance =0
                minvalue = ""
                for vector in pertenencias[clusterNumb]:
                    distance3 =distance.calcularDistancia(distance, dist, vectorData[vector], values)
                    if (distance3 < mindistance or mindistance == 0):
                        minvalue = vector
                        mindistance= distance3
                doc.write(name+"\n"+
                          "cluster: "+str(clusterNumb)+"\n"+
                          " nearest instance:  "+minvalue+"\n"+
                          "-------------------------------------------------------------------\n")
            else:
                doc.write(name + "\n" +
                          "cluster: " + str(clusterNumb) + "\n" +
                          " nearest instance: NaN \n" +
                          "-------------------------------------------------------------------\n")

if __name__ == "__main__":
    if len(sys.argv)==5:
        newClusterization(sys.argv[1], sys.argv[2], sys.argv[3],sys.argv[4])
    else:
        print("La cantidad de atributos es incorrecta.\n"+
              "Este programa clusteriza instancias no vistas anteriormente y nos indica cual es la instancia mas cercana\n"+
              "Paramentros:\n"+
              "1.- path al modelo de clustering.\n"+
              "2.- path a los datos de entrenamiento\n"+
              "3.-path al archivo que contiene la/las nuevas instancias a clusterizar.\n"+
              "4.-path al archivo en el que se guardara la respuesta.")
