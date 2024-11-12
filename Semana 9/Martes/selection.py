def main():
    lista = [6,5,3,1,8,7,4,2]
    lista = selection(lista)
    print(lista)

def selection(lista):
    for i in range(len(lista)):#n
        minor = i #n
        for j in range(i+1,len(lista)): #n2
            if lista[j] < lista[minor]: #n2
                minor = j #n2
        temp = lista[i] #n
        lista[i] = lista[minor] #n
        lista[minor] = temp #n
        #3n2 + 5n = O(n2)
    return lista    

main()

