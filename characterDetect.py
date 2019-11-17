import sys
def remove(datos):
    with open(datos, 'r') as doc:
        newdoc = open("caracters.txt", 'w+')
        caracters = []
        for lerroa in doc:
            new2line = lerroa.split(",")
            for char in  new2line[2]:
                if char not in caracters:
                    caracters.append(char)
        newdoc.write(str(caracters))
if __name__ == "__main__":
    if len(sys.argv) == 2:
        remove(sys.argv[1])
    else:
        print("La cantidad de atributos es incorrecta.\n" +
              "Crea una lista con los caractere contenidos en el texto y los guarda en caracteres.txt\n" +
              "Paramentros:\n" +
              "1.- path a los datos")