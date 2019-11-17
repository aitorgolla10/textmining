from gensim.models.doc2vec import Doc2Vec ,TaggedDocument
from gensim.test.utils import get_tmpfile
import sys
def genModel(dataset):
    with open(dataset, 'r') as doc:
        docs = []
        for lerro in doc:
            lerroSplit = lerro.split(",")
            words = lerroSplit[1].split()
            tags = [lerroSplit[0]]
            docs.append(TaggedDocument(words, tags))

        model = Doc2Vec(docs, vector_size = 300, window = 300, min_count = 1, workers = 4)
        model.save("mymode1")
if __name__ == "__main__":
    if len(sys.argv) == 2:
       genModel(sys.argv[1])
    else:
        print("La cantidad de atributos es incorrecta.\n" +
              "Este programa genera un modelo doc2vec en el archivo mymodel1 con los datos del dataset proporcionado\n" +
              "Paramentros:\n" +
              "1.-path a los datos para generar el modelo")