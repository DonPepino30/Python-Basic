"""13. Haciendo el uso de *args y **kwargs aplicarlo debidamente para usar
decorar una función que recibirá 4 argumentos los cuales se
multiplicaran entre ellos.
Mensaje previo al usar el decorador “Está por ejecutarse la función” y
mensaje luego de usar el decorador “La función ha sido ejecutado
correctamente”"""

def multiplicadorD(*args):
    def funcB(func):
        def funcC(*kwargs):
            print("Está por ejecutarse la función")
            resultado = func(*args, *kwargs)
            print("La función ha sido ejecutada correctamente")
            return resultado
        return funcC 	
    return funcB

@multiplicadorD(4, 5, 6, 7)
def multiplicar(*num):
    return num[0] * num[1] * num[2] * num[3]
print(multiplicar(3, 2, 1, 0))
