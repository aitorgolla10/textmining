from gensim.models.doc2vec import Doc2Vec,TaggedDocument
import sys
model = Doc2Vec.load('mymode1')
newData = []
with open(sys.argv[1], 'r') as doc:
    file = open(sys.argv[1].replace(".txt",".csv").replace("raw","doc2vec"),"w")
    for lerro in doc:
        lerro = lerro.replace("b'","").replace("'","")
        lerroSplit = lerro.split(",")
        words = lerroSplit[1].split()
        result = model.infer_vector(words)
        result = result.tolist()
        file.write(lerroSplit[0]+","+",".join(str(v) for v in result)+"\n")