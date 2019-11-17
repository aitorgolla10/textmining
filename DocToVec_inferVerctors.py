from gensim.models.doc2vec import Doc2Vec,TaggedDocument
import sys
def inferVector(data):
    model = Doc2Vec.load('mymode1')
    newData = []
    with open(data, 'r') as doc:
        file = open(sys.argv[1].replace(".txt",".csv").replace("raw","doc2vec"),"w")
        for lerro in doc:
            lerro = lerro.replace("b'","").replace("'","")
            lerroSplit = lerro.split(",")
            words = lerroSplit[1].split()
            result = model.infer_vector(words)
            result = result.tolist()
            file.write(lerroSplit[0]+","+",".join(str(v) for v in result)+"\n")
if __name__ == "__main__":
    if len(sys.argv) == 2:
       inferVector(sys.argv[1])
    else:
        print("La cantidad de atributos es incorrecta.\n" +
              "Este programa transforma los datos representando el texto mediante vectores generados por el modelo doc2vec mymode1\n" +
              "Paramentros:\n" +
              "1.-path a los datos que se quieren transformar")