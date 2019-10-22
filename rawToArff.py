import sys

doc = open("rawTOarfffile.arff", 'w+')
with open(sys.argv[1], 'r') as orig:
    doc.write("@relation rawTOarffFile\n\n"
              "@attribute _newid_ numeric\n"
              "@attribute _module_ { Adult, Child, Neonate }\n"
              "@attribute _open_response_ string\n"
               "\n@data\n")

    next(orig)
    for lerroa in orig:
        doc.write(lerroa)