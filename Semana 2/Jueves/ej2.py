age = input("Please enter your age:")
if age.isnumeric():
    age = int(age)
    aux = 1
    while aux <= age:
        print(aux)
        aux += 1