import pandas as pd
import csv
from distantziak import  Distantziak as distance



class KMeans():

    def kmeans(k, distancia, archivoDestino):

        pertenencias = {}       # HashMap identificador --> cluster al que pertenece
        vectores = {}

        with open('doc2vectrain.csv') as trainCsv:
            data = csv.reader(trainCsv, delimiter=',')
            for lerroa in data:
                #print(' '.join(lerroa))
                pertenencias[lerroa[0]] = 'cluster1'
                vectores[lerroa[0]] = lerroa[1:]

            distantzia = distance.coseno(vectores['1710 Child'],vectores['6063 Adult'])
            print("Distancia entre los vectores -->")
            print(distantzia)













