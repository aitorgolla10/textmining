import sys
with open(sys.argv[1], 'r') as doc:
    print(doc)
    removableChars = []
    for lerroa in doc:
        print(lerroa)
        lerroGarbia = lerroa[1:-2].replace("'","")
        for char in lerroGarbia.split(','):
            removableChars.append(char)
newdoc = open("FinalPreArfffData.txt", 'w+')
with open(sys.argv[2], 'r') as doc:
    for lerroa in doc:
        newline = lerroa.replace("'","")
        new2line = newline.split(",")
        for character in removableChars:
            new2line[2]= new2line[2].replace(character,"")
        newline = ",".join(new2line)
        newdoc.write(newline)
