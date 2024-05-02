"""Crear una función que aceptará por parámetro dos valores que serán
ingresados por el usuario, una lista donde los valores serán llenados
por el usuario también y un segundo parámetro que eliminará de la
lista que fue ingresada a la función, finalmente el output de la función
será la lista actualizada sin el valor que se sacará de la lista. Mostrar
también la lista original y el número que fue eliminado."""

def removerValor(lista, valor):
    listaOriginal = lista.copy()
    lista.remove(valor)
    print(f"Lista inicial: {listaOriginal}")
    print(f"Nueva lista: {lista}")
def main():
    lista1 = []
    cant = int(input("Cuantos numeros desea añadir a la lista?: "))
    for i in range(cant):
        valor = int(input(f"Enter element {i+1}: "))
        lista1.append(valor)
    valorPorEliminar = int(input("Ingrese el valor a eliminar: "))
    if valorPorEliminar in lista1:
        removerValor(lista1, valorPorEliminar)
    else:
        print("El valor no se encuentra en la lista")
        return 0
if __name__ == "__main__":
    main()