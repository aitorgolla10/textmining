import numpy as np


class Distantziak():

    def euclidean(vector1,vector2):         # Le asignamos el valor 0
        dist = 0
        for i in range(0,len(vector1)):
            dist += (float(vector1[i]) - float(vector2[i]))**2
        distance = dist**(1/2)
        return  distance

    def manhattan(vector1, vector2):        # Le asignamos el valor 1
        dist = 0
        for i in range(0,len(vector1)):
            dist += abs((float(vector1[i]) - float(vector2[i])))
        #dist = vector1-vector2
        return  abs(dist)

    def coseno(vector1, vector2):           # Le asignamos el valor 2
        dist = 0
        batukari = 0
        biderketa = 0
        bat = 0
        bi = 0
        for i in range(0, len(vector1)):
            batukari += (float(vector1[i])*float(vector2[i]))
            bat += float(vector1[i])**2
            bi += float(vector2[i]) ** 2

        bat = float(bat)**(1/2)
        bi = float(bi)**(1/2)
        biderketa = bat*bi
        dist = batukari/biderketa

        return dist


    def calcularDistancia(self,distantzia, vector1, vector2):

        if (distantzia == 0):

            distantzia = self.euclidean(vector1,vector2)

        elif (distantzia == 1):

            distantzia = self.manhattan(vector1, vector2)


        elif (distantzia == 2):

            distantzia = self.coseno(vector1, vector2)

        else:

            print("No has introducido bien la distancia")
            distantzia = -1

        return distantzia

    def calcularMedia(self,v):

        tamaño = len(v)

        if (tamaño==0):
            print("Este cluster no tiene ninguna instancia")
            return -1
        else:

            suma = []
            x = 0
            for i in range(0,len(v[1])):
                suma.append(0)
            i = 0

            while (i<tamaño):
                suma = self.sumaDeVectores(suma,v[i])
                i = i+1

            while (x<len(suma)):
                suma[x] = float(suma[x]) / float(tamaño)
                x = x+1
            return suma




    def sumaDeVectores(v1, v2):

        resultado = []
        i = 0
        tamaño = len(v1)
        if tamaño==0:
            print("Este cluster no tiene ninguna instancia")
            return -1

        while (i<tamaño):
            resultado.append(float(v1[i]) + float(v2[i]))
            i = i+1
        return resultado





