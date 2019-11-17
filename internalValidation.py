import sys
import csv
import sklearn.metrics
import numpy as np
from distantziak import  Distantziak as distance
def dabies(result,model,dataset):
    doc = open(result,'a+')#resultados
    cluster = open(model,'r') #cluster model
    vectores =[]
    with open(dataset) as trainCsv:
        data = csv.reader(trainCsv, delimiter=',')
        clust = cluster.readlines()
        k = int(clust[0])
        dist = int(clust[1])
        centroid = []
        pertenencias = []
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
        daviesVowin = 0
        for i in range(k):
            valuesToMax = []
            mediaI =0
            if(len(newPetenencias[i]) != 0):
                for intantzia in newPetenencias[i]:
                    mediaI +=  distancias[intantzia+str(i)]
                mediaI = mediaI/len(newPetenencias[i])

            for j in range(k):
                if j != i:
                    mediaj =0
                    if(len(newPetenencias[j])!=0):
                        for instance in newPetenencias[j]:
                            mediaj += distancias[instance+str(j)]
                                #distance.calcularDistancia(distance,dist,vectorData[instance],clusterCentroids[i])
                        mediaj = mediaj/len(newPetenencias[j])
                    clusterdistance = distance.calcularDistancia(distance,dist,clusterCentroids[j],clusterCentroids[i])
                    if clusterdistance != 0 :
                         valuesToMax.append((mediaI+mediaj)/clusterdistance)
            maxValue = max(valuesToMax)
            daviesVowin += maxValue
        daviesVowin = daviesVowin/k
        doc.write(sys.argv[2]+","+str(daviesVowin)+"\n")
        print("daciesVowin value:  "+str(daviesVowin))

            #value = sklearn.metrics.davies_bouldin_score(nsamples2,clusterCentroids)
        #doc.write(sys.argv[2]+","+str(value))

if __name__ == "__main__":
    if len(sys.argv) == 4:
       dabies(sys.argv[1],int(sys.argv[2]),int(sys.argv[3]))
    else:
        print("La cantidad de atributos es incorrecta.\n" +
              "Este programa calcula el indicador daviesVowin para los clusters generados\n" +
              "Paramentros:\n" +
              "1.- archivo donde guardar resultados.\n" +
              "2.-path al modelo\n" +
              "3.-dataset de entrenamiento")

