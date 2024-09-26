height = int(input("Please enter the height:"))
aux = 1
while aux <= height*2:
    if aux == 1:
        print(aux)
    else:
        print(aux, end=" ")
    for number in range(aux-2,0,-2):
        if number == 1:
            print(number)
        else:
            print(number, end=" ")
    aux += 2
