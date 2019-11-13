import matplotlib.pyplot as plt
import csv
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import numpy as np
from distantziak import  Distantziak as distance
import sys
import random

class Visualizacion():

    def visualizarClusters(model, dataset):


        cluster = open(model, 'r')  # cluster model
        vectores = []
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
                j = j+1
            distancias = {}
            vectorData = {}

            # cargar centroides
            for cent in range(2, k + 2):
                newCentroid = clust[cent][1:-2]
                centroid.append(newCentroid.split(","))
            clusterCentroids = np.array(centroid)
            clusterCentroids = clusterCentroids.astype(np.float64)

            # cargar vectores y ordenarlos
            for lerroa in data:
                vectorData[lerroa[0]] = lerroa[1:]
                vectores.append(lerroa[0])
            for v in vectores:
                z = 0
                distancia = 0

                while z < k:

                    distancia2 = distance.calcularDistancia(distance, dist, clusterCentroids[z], vectorData[v])
                    distancias[v + str(z)] = distancia2
                    if (distancia2 < distancia or distancia == 0):
                        distancia = distancia2
                        c = z
                    z = z + 1

                pertenencias[c].append(vectorData[v])


            with open('visualizacion.csv', 'w') as csvFile:
                writer = csv.writer(csvFile)
                i = 0
                cantidadInstancias = []
                while (i<len(pertenencias)):
                    writer.writerows(pertenencias[i])
                    cantidadInstancias.append(len(pertenencias[i]))
                    i = i+1

                z = 1
                columnas = []
                while (z < 301):
                    columnas.append(z)
                    z = z+1

                index = []
                i = 0
                while (i < len(pertenencias)): #Conseguir los identificadores de los documentos ordenados por clusters
                    j = 0
                    while (j < len(pertenencias[i])):
                        vector = pertenencias[i][j]
                        for linea in vectorData:
                            if (vectorData[linea] == vector):
                                index.append(linea)
                        j = j + 1
                    i = i + 1

                df = pd.read_csv("visualizacion.csv", names=columnas)
                features = columnas
                x = df.loc[:, features].values
                x = StandardScaler().fit_transform(x)
                pd.DataFrame(data=x, columns=features).head()

                pca = PCA(n_components=2)
                principalComponents = pca.fit_transform(x)
                principalDf = pd.DataFrame(data=principalComponents, columns=['Columna 1', 'Columna 2'], index=index)
                print(principalDf.head(5))
                print(principalDf.loc['6063 Adult'])

                fig = plt.figure(figsize=(8, 8))
                ax = fig.add_subplot(1, 1, 1)
                ax.set_xlabel('Columna 1', fontsize=15)
                ax.set_ylabel('Columna 2', fontsize=15)
                ax.set_title('Clustering documentos', fontsize=20)

                tamaño = 20
                contador = 0
                cluster = 0
                colores = k

                color = ["#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
                         for i in range(colores)]

                legend = []
                while contador<len(index):
                    instanciaDelCluster = 0
                    while (instanciaDelCluster < cantidadInstancias[cluster]):
                        cantidadInstancias[c]
                        x = principalDf.loc[index[contador],'Columna 1']
                        y = principalDf.loc[index[contador], 'Columna 2']
                        plt.scatter(x,y,s=tamaño,color=color[cluster])
                        #plt.annotate(index[contador],(x,y))
                        instanciaDelCluster = instanciaDelCluster +1
                        contador = contador+1
                    legend.append(color[cluster])
                    cluster = cluster+1
                i=0


                #plt.legend(legend)
                plt.show()






if __name__ == "__main__":
    Visualizacion.visualizarClusters(sys.argv[1],sys.argv[2])

