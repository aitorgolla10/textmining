
class Distantziak():

    def euclidean(vector1,vector2):         # Le asignamos el valor 0
        dist = 0
        for i in range(0,len(vector1)):
            dist += (vector1[i] - vector2[i])**2
        distance = dist**(1/2)
        return  distance

    def manhattan(vector1, vector2):        # Le asignamos el valor 1
        dist = 0
        for i in range(0,len(vector1)):
            dist += abs((vector1[i] - vector2[i]))
        #dist = vector1-vector2
        return  abs(dist)

    def coseno(vector1, vector2):           # Le asignamos el valor 2
        dist = 0
        batukari = 0
        biderketa = 0
        bat = 0
        bi = 0
        for i in range(0, len(vector1)):
            batukari += (vector1[i]*vector2[i])
            bat += vector1[i]**2
            bi += vector2[i] ** 2

        bat = bat**(1/2)
        bi = bi**(1/2)
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


