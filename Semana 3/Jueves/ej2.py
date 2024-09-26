numero_ingresado = int(input("Please enter a number:"))
is_pronic = False

for number in range(1,numero_ingresado-1):
    if number * (number+1) == numero_ingresado:
        is_pronic = True
        break

if is_pronic:
    print(f"The number {numero_ingresado} is pronic")
else:
    print(f"The number {numero_ingresado} is not pronic")