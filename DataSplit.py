from sklearn.model_selection import train_test_split
import numpy
import sys
def dsplit(dataset):
    with open(dataset, "rb") as f:
        data = f.read().splitlines()
        data = numpy.array(data)  #convert array to numpy type array
        print( len (data))
        x_train ,x_test = train_test_split(data,test_size=0.3)
        numpy.savetxt("rawtrain.txt",x_train, delimiter=',', fmt='%s')
        numpy.savetxt("rawtest.txt", x_test,  delimiter=',', fmt='%s')
if __name__ == "__main__":
    if len(sys.argv)==1:
        dsplit(sys.argv[1])
    else:
        print("La cantidad de atributos es incorrecta.\n" +
              "Este programa separa el dataset en 2 partes de 70% y 30%\n" +
              "Paramentros:\n" +
              "1.- path al archivo a separar")