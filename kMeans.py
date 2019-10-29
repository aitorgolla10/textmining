import pandas as pd



class KMeans():

    def kmeans(archivoCsv, k, distancia, archivoDestino):

        data = pd.read_csv(archivoCsv)
        with open(archivoCsv, "r") as doc:
            for lerro in doc:
                lerroSplit = lerro.split(",")[1:]
                tamaño = len(lerroSplit)

        archivoCsv.split(",")
        centroides = k


