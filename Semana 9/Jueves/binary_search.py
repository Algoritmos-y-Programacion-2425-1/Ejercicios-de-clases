def binary_search(number, lista):
    mid = len(lista) // 2
    if len(lista) == 1:
        if lista[mid] == number:
            return number
        else:
            return -1

    if number == lista[mid]:
        return number
    if (number < lista[mid]):
        return binary_search(number,lista[:mid])
    else:
        return binary_search(number,lista[mid:])

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

def main():
    search_number = input("Please enter a number:")
    if binary_search(int(search_number),selection([6,5,3,1,8,7,4,2])) == -1:
        print(f"The number {search_number} is not present")
    else:
        print(f"The number {search_number} is present")

main()