from kMeans import KMeans as kMeans
import csv
import pandas as pd


kMeans.kmeans("doc2vectrain.csv",3,2)    #  kmeans(número de clusters, distancia tipo)
                        # Distancia tipo: 0 --> euclidea
                        #                 1 --> manhattan
                        #                 2 --> coseno

    #data = pd.read_csv(csvFile)
    #data_top = data.head()      # Hasierako balioak agertzeko
    #   df = pd.DataFrame(data=data)
    #print(data.loc[:,'open_response']) # Testuko zutabea bakarrik agertzeko

