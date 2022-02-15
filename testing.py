import Modelo as mod

while(True):
    q = input(".Realiza una pregunta\n -Escribe quit para salir.\n")
    if(q == 'quit'):
        break
    x =  mod.consulta(q)
    print(x)