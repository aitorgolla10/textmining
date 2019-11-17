import sys
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