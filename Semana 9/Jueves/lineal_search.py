def search_in_list(number, lista):
    for element in lista:
        if element == number:
            return number
    return -1

def main():
    search_number = input("Please enter a number:")
    if search_in_list(int(search_number),[6,5,3,1,8,7,4,2]) == -1:
        print(f"The number {search_number} is not present")
    else:
        print(f"The number {search_number} is present")

main()