import pandas as pd
import csv
from numpy import random

from distantziak import  Distantziak as distance



class KMeans():

    def kmeans(k, distancia, archivoDestino):

        i = 0;
        j = 0;
        pertenencias = {}       # HashMap identificador --> cluster al que pertenece
        vectores = {}
        identificadores = []
        idCentroides = []
        centroides = []
        vectoresSolos = []

        with open('doc2vectrain.csv') as trainCsv:
            data = csv.reader(trainCsv, delimiter=',')

            for lerroa in data:
                #print(' '.join(lerroa))

                identificadores.append(lerroa[0])
                pertenencias[lerroa[0]] = 'Sin cluster'
                vectores[lerroa[0]] = lerroa[1:]
                vectoresSolos.append(lerroa[1:])
                i = i+1
            centroidesNuevos = []
            clustersTodos = []
            while j<k:
                cluster = []
                clustersTodos.append(cluster)
                centroidesNuevos.append(cluster)
                idCentroides.append(random.choice(identificadores))     #Escoger centroides aleatorios
                centroides.append(vectores[idCentroides[j]])            #Inicializar centroides
                j = j+1


            iteraciones = 0

            while (iteraciones<5):
                id = 0
                #COPIAR CENTROIDES NUEVOS EN CENTROIDES VIEJOS
                for v in vectoresSolos:
                        z = 0
                        distancia = 0

                        while z<k:

                            distancia2 = distance.calcularDistancia(distance,1,centroides[z],v)
                            if (distancia2 < distancia or distancia==0):
                                distancia = distancia2
                                c = z
                            z = z+1

                        pertenencias[identificadores[id]] = 'Cluster' + str(c+1)
                        id = id+1
                        clustersTodos[c].append(v)

                w=0
                while (w<k):                #Actualizar centroides calculando la media

                    centroidesNuevos[w] = distance.calcularMedia(distance,clustersTodos[w])
                    w = w+1

                print(centroides)
                print(centroidesNuevos)
                iteraciones = iteraciones+1








            #distantzia = distance.coseno(vectores['1710 Child'],vectores['6063 Adult'])
            #print("Distancia entre los vectores -->")
            #print(distantzia)

















