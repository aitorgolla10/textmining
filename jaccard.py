class Jaccard():
    def jaccard_similarity(list1, list2):
        intersection = len(list(set(list1).intersection(list2))) # calculo del Índice de Jaccard
        union = (len(list1) + len(list2)) - intersection
        jaccardIndex= float(intersection) / union
        jaccardDistance= float(1-jaccardIndex)
        print("JaccardIndex = " + str(jaccardIndex))
        print("JaccardDistance = " + str(jaccardDistance))
        return jaccardIndex