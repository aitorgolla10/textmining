import pandas as pd
from distantziak import  Distantziak as distance



class KMeans():

    def kmeans(archivoCsv, k, distancia, archivoDestino):

        centroides = k
        data = pd.read_csv(archivoCsv)
        print(data.loc[:, 'open_response'])  # Testuko zutabea bakarrik agertzeko
        print(centroides)
        print(distancia)
        #with open(archivoCsv, "r") as doc:
            #for lerro in doc:
                #vector = lerro.split(",")[1:]

                #for i in k:

                    #distance.calcularDistancia(distancia)







