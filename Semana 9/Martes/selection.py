def main():
    lista = [6,5,3,1,8,7,4,2]
    lista = selection(lista)
    print(lista)

def selection(lista):
    for i in range(len(lista)):
        minor = i
        for j in range(i+1,len(lista)):
            if lista[j] < lista[minor]:
                minor = j
        temp = lista[i]
        lista[i] = lista[minor]
        lista[minor] = temp
        
    return lista    

main()

