def main():
    lista = quicksort([6,5,3,1,8,7,4,2])
    print(lista)

def quicksort(lista):
    if len(lista) < 2:
        return lista
    menor, pivote, mayor = partition(lista)
    return quicksort(menor) + [pivote] + quicksort(mayor)

def partition(lista):
    menor = []
    mayor = []
    pivote = lista[0]
    for number in lista:
        if number < pivote:
            menor.append(number)
        elif number > pivote:
            mayor.append(number)
    return menor, pivote, mayor

main()