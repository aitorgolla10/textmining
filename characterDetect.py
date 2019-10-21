import sys
with open(sys.argv[1], 'r') as doc:
    newdoc = open("caracters.txt", 'w+')
    caracters = []
    for lerroa in doc:
        new2line = lerroa.split(",")
        for char in  new2line[2]:
            if char not in caracters:
                caracters.append(char)
    newdoc.write(str(caracters))