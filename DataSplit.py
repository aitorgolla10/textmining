from sklearn.model_selection import train_test_split
import numpy
import sys

with open(sys.argv[1], "rb") as f:
    data = f.read().splitlines()
    data = numpy.array(data)  #convert array to numpy type array
    print( len (data))
    x_train ,x_test = train_test_split(data,test_size=0.3)
    numpy.savetxt("rawtrain.txt",x_train, delimiter=',', fmt='%s')
    numpy.savetxt("rawtest.txt", x_test,  delimiter=',', fmt='%s')
