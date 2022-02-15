from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel
import Modelo as mod
'''
Para poder ejecutar el código:
Tener instaldo uvicorn y fastapi
Comando:
> uvicorn mainapp:app --reload
'''

app = FastAPI()

@app.get("/get-an-input/")
def getQuestion(question: Optional[str] = None):
    #Aquí va el pocesamiento de la pregunta por parte del modelo 
    cat = "Out"
    if question == None:
        question = "Hola soy un chatbot, puedes hacerme preguntas acerca del servcio social :)"
    elif question == "Adios":
        question = "Hasta luego!"
    
    cat, question = mod.consulta(question)
    
    return {cat : question}