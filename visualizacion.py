import matplotlib.pyplot as plt
import csv
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import numpy as np
from distantziak import  Distantziak as distance
import sys
import random
import matplotlib.patches as mpatches

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
                while (i<len(pertenencias)):                   # Guardar la cantidad de instancias de cada cluster
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
                while (i < len(pertenencias)):          #Conseguir los identificadores de los documentos ordenados por clusters
                    j = 0
                    while (j < len(pertenencias[i])):
                        vector = pertenencias[i][j]
                        for linea in vectorData:
                            if (vectorData[linea] == vector):       # Conseguir el identificador del vector
                                index.append(linea)                 # Guardar identificador
                        j = j + 1
                    i = i + 1


                df = pd.read_csv("visualizacion.csv", names=columnas)
                features = columnas
                x = df.loc[:, features].values
                x = StandardScaler().fit_transform(x)
                pd.DataFrame(data=x, columns=features).head()

                pca = PCA(n_components=2)                           # Conversión a 2 atributos para visualización 2D
                principalComponents = pca.fit_transform(x)
                principalDf = pd.DataFrame(data=principalComponents, columns=['Atributo 1', 'Atributo 2'], index=index)


                fig = plt.figure(figsize=(8, 8))
                ax = fig.add_subplot(1, 1, 1)
                ax.set_xlabel('Atributo 1', fontsize=15)
                ax.set_ylabel('Atributo 2', fontsize=15)
                ax.set_title('Clustering de documentos (KMeans)', fontsize=20)

                tamaño = 20             # Tamaño del punto
                contador = 0
                cluster = 0
                colores = k             # Misma cantidad de colores y de clusters

                color = ["#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
                         for i in range(colores)]

                legend = []
                while contador<len(index):  # Meter un punto en el gráfico por cada documento (instancia)
                    instanciaDelCluster = 0
                    while (instanciaDelCluster < cantidadInstancias[cluster]): # Recorrer las del mismo cluster para asignar
                        cantidadInstancias[c]                                   # mismo color
                        x = principalDf.loc[index[contador],'Atributo 1']
                        y = principalDf.loc[index[contador], 'Atributo 2']
                        plt.scatter(x,y,s=tamaño,color=color[cluster])          # Añadir el punto con sus dos atributos y color
                        #plt.annotate(index[contador],(x,y), size=4)
                        instanciaDelCluster = instanciaDelCluster +1
                        contador = contador+1
                    cluster = cluster+1

                # Personalizar las legend (cuadrado informativo) cada cluster con su color
                patch = []
                z = 0
                while (z < colores):
                    etiqueta = mpatches.Patch(color=color[z], label='Cluster ' + str(z+1))
                    patch.append(etiqueta)
                    z = z+1

                plt.legend(handles=patch)

                plt.show()

                # IMPRIMIR IDENTIFICADORES POR CLUSTER PARA POSTERIORES COMPARACIONES

                contador = 0
                j = 0
                while contador<len(index):
                    i = 0
                    clusterCantidad = cantidadInstancias[j]
                    print(" ")
                    print("================")
                    print("CLUSTER " + str(j+1))
                    print("================")
                    while i < clusterCantidad:
                        print(index[contador] + ", " , end=' ')
                        contador = contador +1
                        i = i+1
                    j = j+1






# Para ejecutar la visualización 2 argumentos: --> 1: modelo del clustering (KclustersWithXmodel)
#                                              --> 2: conjunto de entrenamiento (doc2vectrain.csv)

# Ejemplo: python visualizacion.py 10clustersWith0model doc2vectrain.csv


if __name__ == "__main__":
    Visualizacion.visualizarClusters(sys.argv[1],sys.argv[2])

