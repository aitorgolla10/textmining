from kMeans import KMeans as kMeans
import csv
import pandas as pd

with open('/home/aitor/Descargas/cleaned_PHMRC_VAI_redacted_free_text.test_blind (2).csv') as csvFile:

    kMeans.kmeans(3, "euclidean", "eee")

    #data = pd.read_csv(csvFile)
    #data_top = data.head()      # Hasierako balioak agertzeko
    #   df = pd.DataFrame(data=data)
    #print(data.loc[:,'open_response']) # Testuko zutabea bakarrik agertzeko

