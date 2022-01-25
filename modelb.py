from sentence_transformers import SentenceTransformer
import torch
import numpy as np


'''
Para usar es necesario tener instalado pytorch, transformers y Sentence-Transformers
> pip install pytorch
> pip install transformers 
> pip install -U sentence-transformers
'''

def distance(x, y): # Función de norma 1 entre tensores
    x = torch.from_numpy(x)
    y = torch.from_numpy(y)
    return torch.sum(abs(x-y)).item()

# Oraciones a contrastar
sentences = ["Tienes que contar con al menos el 70 porciento de créditos totales en DGAE-SIAE, al momento de iniciar el proceso de registro del Servicio Social.Sólo podrás realizar tu servicio social en alguna institución pública o en organismos no gubernamentales sin fines de lucro, que tengan programas registrados y aprobados para tu licenciatura.", 
             "La duración mínima es de 6 meses de trabajo efectivo y máxima de un año calendario, debiendo cubrir un total de 480 horas.",
             "Si ya cuentas con el 70 porciento de créditos ingresa al siguiente link https://www.siass.unam.mx/ para ver los programas aprobados para tu licenciatura.Debes tener en cuenta lo siguiente:-Verifica los lugares disponibles para tu carrera. Si hay lugares disponibles, ponte en contacto con el responsable del programa.-Los programas son anuales. Estos se registran en el periodo de noviembre - marzo.-Sólo podrás realizar el servicio social en institución pública o en organismos no gubernamentales sin fines de lucro. Una vez que escojas un programa de servicio social que te interese, contacta al la Institución. En el SIASS puedes encontrar los datos del contacto del Responsable de Servicio Social del programa, esta es la persona con la que te tienes que dirigir."]

# Modelo
model = SentenceTransformer('hiiamsid/sentence_similarity_spanish_es')
embeddings = model.encode(sentences)
# print(embeddings)

# Consulta
q = ["¿Cuántas horas son?"]
query = model.encode(q)


index = 1
print("Oraciones: ")
for s in sentences:
    print(str(index) + ".- " + s)
    index += 1
    
print("Consulta :" + q[0])

print("Distancia:" ) 
d = (0, 1e9)
for i in range(embeddings.shape[0]):
    t = distance(embeddings[i], query[0])
    if t<d[1]:
        d = (i+1, t)
    print("Distancia entre la oración " + str(i+1) + " y la consulta: " + str(t))
    
print("La oración con distancia más corta con la consulta es :\n" + str(sentences[d[0]]) + "\nCon  distancia: " + str(d[1]))

print('---'*50)
print(query.shape)
print(embeddings.shape)
print(type(query))
def cosine_similarity(x, y):
    return np.matmul(x, y) / (np.linalg.norm(x, axis=1) * np.linalg.norm(y))
#(np.linalg.norm(List1, axis=1) * np.linalg.norm(List2))


print(cosine_similarity(query, np.matrix.transpose(embeddings)))
