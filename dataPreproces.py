import sys
def filter(data):
    newdoc = open("removedColumsFiltered.txt", 'w+')
    with open(sys.argv[1], 'r') as doc:
        for lerroa in doc:
            newline = lerroa.replace("'","")
            new2line = newline.split(",")
            new2line[2] = new2line[2].encode("ascii", errors="ignore").decode()
            new2line[2] = new2line[2].replace("  ", " ")
            new2line[2] = new2line[2].lower()
            newline = ",".join(new2line)
            newdoc.write(newline)

if __name__ == "__main__":
    if len(sys.argv)==2:
        filter(sys.argv[1])
    else:
        print("La cantidad de atributos es incorrecta.\n" +
              "Este programa se asegura de qque todos los datos esten es codificaccion ASCIIy los devuelve  en el archivo removedColumsFiltered.txt\n" +
              "1.- path a los datos.")