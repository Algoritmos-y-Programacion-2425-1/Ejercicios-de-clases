def exponential(base, power):
    if (power < 1):
        return 1
    return base * exponential(base, power - 1)

def isPrime(number,aux):
    if number < 2:
        return False
    if number % aux == 0:
        if number == 2:
            return True
        else:
            return False
    if aux == (number -1):
        return True
    return isPrime(number, aux+1)

def reverse_word(word,index):
    if word == "":
        return ""
    if index == 0:
        return word[index]
    return word[index] + reverse_word(word, index-1)

def main():
    while True:
        option = input("What do you want to do? \n1- Exponential\n2- Prime\n3- Fibonacci\n4- Reverse word\n5- Exit\n->")
        if option == "1":
            result = exponential(int(input("Please enter the base: ")), int(input("Please enter the power: ")))
            print(f"The result is {result}")
        elif option == "2":
            if isPrime(int(input("Please enter the number: ")),2):
                print("Is prime")
            else:
                print("Is not prime")
        elif option == "3":
            pass
        elif option == "4":
            word = input("Please enter a word: ")
            print(reverse_word(word,len(word)-1))
        elif option == "5":
            break
        else:
            print("Invalid Option")
main()

