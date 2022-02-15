from sentence_transformers import SentenceTransformer
import numpy as np
import json
'''
Para usar es necesario tener instalado numpy, transformers y Sentence-Transformers
> pip install transformers 
> pip install -U sentence-transformers
> pip install numpy
'''

# Cargando modelo
model = SentenceTransformer('hiiamsid/sentence_similarity_spanish_es')

def ToString(i):
    return list(data[i].values())[0]

# Leyendo json
with open('categoriasV1.json', 'r', encoding="utf-8") as file:
    data = json.load(file)
    # Tratamiento de oraciones
    l = len(data)
    # l = 3
    sentences = []
    for i in range(l):
        sentences.append(ToString(i).strip('\n'))
    # Transformado oraciones
    embeddings = model.encode(sentences)
    print(embeddings.shape)
    # Guardando arreglo
    np.save('zero_sentence.npy', embeddings)
    
    # Cargar arreglo
    # a = np.load('zero_sentence.npy')
    
