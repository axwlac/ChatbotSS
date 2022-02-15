from sentence_transformers import SentenceTransformer
import numpy as np
import json

with open('categoriasV1.json', 'r', encoding="utf-8") as file:
    data = json.load(file)

def cosine_similarity(x, y):
    return np.matmul(x, y) / (np.linalg.norm(x, axis=1) * np.linalg.norm(y))


def consulta(string):
    # Transformar la consulta 
    model = SentenceTransformer('hiiamsid/sentence_similarity_spanish_es')
    sa = [string]
    st = model.encode(sa)
    
    # Cargando el arreglo de preprocesamiento
    a = np.load('zero_sentence.npy')
    
    # Creacion de distancia
    #print(cosine_similarity(query, np.matrix.transpose(embeddings)))
    v = cosine_similarity(st, np.matrix.transpose(a))
    
    # Encontrando el indice con valor minimo
    
    i = np.where(v == np.amax(v))
    i = np.array(i)
    j = i[1][0].astype(int)
    # print(i)
    return list(data[j-1].keys())[0], list(data[j-1].values())[0]
