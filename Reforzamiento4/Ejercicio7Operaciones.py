import random
def crearLista():
    list1 = []
    for i in range(30):
        list1.append(random.uniform(0,100))
    return list1

def ordenarlista(lista = []):
    lista.sort()
    return lista