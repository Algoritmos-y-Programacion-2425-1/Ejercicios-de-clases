def main():
    lista = [6,5,3,1,8,7,4,2]
    lista = insertion(lista)
    print(lista)

def insertion(lista):
    for i, number in enumerate(lista):
        j = i - 1
        while j >= 0 and number < lista[j]:
            lista[i] = lista[j]
            lista[j] = number
            i -= 1
            j -= 1
    return lista    



main()

