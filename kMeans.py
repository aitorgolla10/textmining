import pandas as pd

import csv
from numpy import random
import sys
from distantziak import  Distantziak as distance

class KMeans():

    def kmeans(file,k, distanciaTipo):

        i = 0;
        j = 0;
        pertenencias = {}       # HashMap identificador --> cluster al que pertenece
        vectores = {}
        identificadores = []
        idCentroides = []
        centroides = []
        vectoresSolos = []

        with open(file) as trainCsv:
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
            cambio = 999
            while (iteraciones<10 and centroides!=centroidesNuevos): #aldaketa < 0.05
                id = 0
                j = 0
                while j < k:
                    clustersTodos[j].clear()
                    j = j+1

                #COPIAR CENTROIDES NUEVOS EN CENTROIDES VIEJOS
                if iteraciones!=0:
                    cambio = 0
                    for i in range(len(centroidesNuevos)):
                        cambio += distance.calcularDistancia(distance,distanciaTipo,centroidesNuevos[i], centroides[i])
                    centroides = centroidesNuevos.copy()
                for v in vectoresSolos:
                        z = 0
                        distancia = 0

                        while z<k:

                            distancia2 = distance.calcularDistancia(distance,distanciaTipo,centroides[z],v)
                            if (distancia2 <= distancia ):
                                distancia = distancia2
                                c = z
                            z = z+1

                        pertenencias[identificadores[id]] = 'Cluster' + str(c+1)
                        id = id+1
                        clustersTodos[c].append(v)

                w=0
                while (w<k):                #Actualizar centroides calculando la media
                    if(len(clustersTodos[w])>0):
                        centroidesNuevos[w] = distance.calcularMedia(distance,clustersTodos[w])
                        w = w+1
                    else: # Para clusters vacíos
                        centroideLejano = distance.instanciaMasLejana(distance,distanciaTipo,vectoresSolos,centroides)
                        centroidesNuevos[w] = centroideLejano
                #print(pertenencias)
                iteraciones = iteraciones+1

            #print("====================")
            u = 0
            while(u<k):
                clusterZenb = u+1
                print("CLUSTER " + str(clusterZenb) + ": " +str(len(clustersTodos[u]))+ " instancias")
                u = u+1

            instanciasTotales = 0
            u = 0
            while (u < k):
                instanciasTotales = instanciasTotales + len(clustersTodos[u])
                u = u+1

            #print("====================")
            u = 0
            while (u < k):

                clusterZenb = u + 1
                instanciasCluster = len(clustersTodos[u])
                porcentaje = round((instanciasCluster/instanciasTotales)*100, 2)
                print("CLUSTER " + str(clusterZenb) + ": %"+str(porcentaje))
                u = u+1
            clusterModel = open(str(k)+"clustersWith"+str(distanciaTipo)+"model",'w+')
            clusterModel.write(str(k)+'\n'+str(distanciaTipo)+'\n')
            for centroid in centroides:
                clusterModel.write(str(centroid)+'\n')

if __name__ == "__main__":
    KMeans.kmeans(sys.argv[1],int(sys.argv[2]),int(sys.argv[3]))





















