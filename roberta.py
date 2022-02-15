from transformers import pipeline
qa_pipe = pipeline("question-answering", model='PlanTL-GOB-ES/roberta-base-bne-sqac')
f = open("informacion.txt",encoding="UTF-8")
context = f.read()
question = "¿A partir de cuántos créditos puedo iniciarlo?"

print(qa_pipe({'context':context, 'question': question}))
# It outpus





