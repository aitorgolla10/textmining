import sys
def removeCaracteres(datos, caracteres):
    with open(datos, 'r') as doc:
        print(doc)
        removableChars = []
        for lerroa in doc:
            print(lerroa)
            lerroGarbia = lerroa[1:-2].replace("'","")
            for char in lerroGarbia.split(','):
                removableChars.append(char)
    newdoc = open("FinalPreArfffrawData2Atrib.txt", 'w+')
    with open(caracteres, 'r') as doc:
        for lerroa in doc:
            newline = lerroa.replace("'","")
            new2line = newline.split(",")
            for character in removableChars:
                new2line[2]= new2line[2].replace(character,"")
            newLine3 =new2line[0]+" "+new2line[1]+","+new2line[2]
            newdoc.write(newLine3)
if __name__ == "__main__":
    if len(sys.argv) == 3:
        removeCaracteres(sys.argv[1],sys.argv[2])
    else:
        print("La cantidad de atributos es incorrecta.\n" +
              "Elimina de los datos los caracteres seleccionados y devuelve un fichero llamado FinalPreArfffrawData2Atrib.txts\n" +
              "Paramentros:\n" +
              "1.- fichero con los caracteres a eliminar\n"+
              "2.- path a los datos")