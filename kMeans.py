import csv
from numpy import random

from distantziak import  Distantziak as distance



class KMeans():

    def kmeans(k, distanciaTipo):

        if k<1:
            print("Incorrecto número de clusters")
            return -1

        if distanciaTipo>2:
            print("Incorrecto tipo de distancia")
            return -1

        i = 0;
        j = 0;

        pertenencias = {}       # HashMap identificador --> cluster al que pertenece
        vectores = {}           # HashMap identificador --> vector
        identificadores = []    # Vector con todos los identificadores
        idCentroides = []       # Vector con los identificadores de los centroides
        centroides = []         # Vectores de los centroides
        vectoresSolos = []      # Todos los vectores de las instancias

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

            while (iteraciones<8):
                id = 0
                if iteraciones>0:
                    centroides = centroidesNuevos              #COPIAR CENTROIDES NUEVOS EN CENTROIDES VIEJOS
                for v in vectoresSolos:
                        z = 0
                        distancia = 0

                        while z<k:

                            distancia2 = distance.calcularDistancia(distance,distanciaTipo,centroides[z],v)
                            if (distancia2 < distancia or distancia==0):
                                distancia = distancia2
                                c = z
                            z = z+1

                        pertenencias[identificadores[id]] = 'Cluster ' + str(c+1)
                        id = id+1
                        clustersTodos[c].append(v)

                w=0
                while (w<k):                #Actualizar centroides calculando la media
                    centroidesNuevos[w] = distance.calcularMedia(distance,clustersTodos[w])
                    w = w+1
                print(pertenencias)
                iteraciones = iteraciones+1

            print("====================")
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

            print("====================")
            u = 0
            while (u < k):

                clusterZenb = u + 1
                instanciasCluster = len(clustersTodos[u])
                porcentaje = round((instanciasCluster/instanciasTotales)*100, 2)
                print("CLUSTER " + str(clusterZenb) + ": %"+str(porcentaje))
                u = u+1






















