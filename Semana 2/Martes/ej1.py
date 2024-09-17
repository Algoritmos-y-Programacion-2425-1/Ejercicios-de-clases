age = input("Please enter your age: ")
if age.isnumeric():
    age = int(age)
    if age >= 18:
        print("You are an adult")
    else:
        print("You are a child")
else:
    print("Error, vuelve a intentar")