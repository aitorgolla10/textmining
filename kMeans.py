import pandas as pd
import csv
from numpy import random
import sys
from distantziak import  Distantziak as distance
from visualizacion import Visualizacion as visualizacion



class KMeans():

    def kmeans(file,k, distanciaTipo):

        if (k<1):                                                          # Tratar excepciones
            print("Has introducido mal el número de clusters")
            exit(0)
        i = 0;
        j = 0;
        pertenencias = {}                           # Diccionario: identificador --> cluster al que pertenece
        vectores = {}                               # Diccionario: identificador --> vector del documento
        identificadores = []                        # Vector con los identificadores de los documentos
        idCentroides = []                           # Vector con los identificadores de los centroides
        centroides = []                             # Vectores de los centroides
        vectoresSolos = []                          # Todos los vectores

        with open(file) as trainCsv:
            data = csv.reader(trainCsv, delimiter=',')

            for lerroa in data:
                #print(' '.join(lerroa))

                identificadores.append(lerroa[0])                   # Añadir identificadores
                pertenencias[lerroa[0]] = 'Sin cluster'             # Inicializar bits de pertenencia
                vectores[lerroa[0]] = lerroa[1:]                    # Añadir ID --> Vector
                vectoresSolos.append(lerroa[1:])                    # Añadir todos los vectores
                i = i+1
            centroidesNuevos = []
            clustersTodos = []

            while j<k:
                cluster = []
                clustersTodos.append(cluster)
                centroidesNuevos.append(cluster)
                idCentroides.append(random.choice(identificadores))     # Escoger centroides aleatorios entre las intsancias
                centroides.append(vectores[idCentroides[j]])            # Inicializar centroides aleatoriamente
                j = j+1


            iteraciones = 0
            cambio = 999
            while (iteraciones<20 and cambio>0.015): #cambio > 0.05    # Hasta que los centroides sean casi iguales o máximo de iteraciones
                id = 0
                j = 0
                while j < k:
                    clustersTodos[j].clear()                           # Inicializar clusters vacíos
                    j = j+1


                if iteraciones!=0:                                     # Copiar centroides nuevos en centroides viejos
                    cambio = 0
                    for i in range(len(centroidesNuevos)):
                        cambio += distance.calcularDistancia(distance,distanciaTipo,centroidesNuevos[i], centroides[i])
                    centroides = centroidesNuevos.copy()

                for v in vectoresSolos:            # Recorrer todas las instancias
                        z = 0
                        distancia = 0

                        while z<k:                 # Calcular distancias vector --> centroides

                            distancia2 = distance.calcularDistancia(distance,distanciaTipo,centroides[z],v)
                            if (distancia2 < distancia or distancia==0):
                                distancia = distancia2
                                c = z                       # Asignar cluster más cercano
                            z = z+1

                        pertenencias[identificadores[id]] = 'Cluster' + str(c+1)
                        id = id+1
                        clustersTodos[c].append(v)       # Añadir en cluster correspondiente

                w=0
                while (w<k):                #Actualizar centroides calculando la media
                    if(len(clustersTodos[w])>0):
                        centroidesNuevos[w] = distance.calcularMedia(distance,clustersTodos[w])
                        w = w+1
                    else:                   # Tratar clusters vacíos
                        centroideLejano = distance.instanciaMasLejana(distance,distanciaTipo,vectoresSolos,centroides)
                        centroidesNuevos[w] = centroideLejano
                iteraciones = iteraciones+1


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

            visualizacion.visualizarClusters(visualizacion,clustersTodos)

if __name__ == "__main__":
    if len(sys.argv) == 4:
        KMeans.kmeans(sys.argv[1],int(sys.argv[2]),int(sys.argv[3]))
    else:
        print("La cantidad de atributos es incorrecta.\n" +
              "Este programa genera un modelo de clustering\n" +
              "Paramentros:\n" +
              "1.- path a los datos de entrenamiento.\n" +
              "2.-cantidad de clusters deseados\n" +
              "3.-Tipo de distancia a utilizar (0 Euclidea, 1 Manhattan,2 Coseno)")






















