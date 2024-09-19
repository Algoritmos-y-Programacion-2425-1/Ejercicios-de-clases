number = int(input("Please enter a number to validate:"))
aux = 2
isPrime = True

if number > 1:
    while aux < number:
        if number % aux == 0:
            isPrime = False
            break
        aux += 1
else:
    isPrime = False

if isPrime:
    print(f"The number {number} is Prime")
else:
    print(f"The number {number} is not Prime")