from gensim.models.doc2vec import Doc2Vec ,TaggedDocument
from gensim.test.utils import get_tmpfile
import sys
with open(sys.argv[1], 'r') as doc:
    docs = []
    for lerro in doc:
        lerroSplit = lerro.split(",")
        words = lerroSplit[1].split()
        tags = [lerroSplit[0]]
        docs.append(TaggedDocument(words, tags))

    model = Doc2Vec(docs, vector_size = 300, window = 300, min_count = 1, workers = 4)
    model.save("mymode1")

