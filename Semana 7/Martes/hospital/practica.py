num = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese segundo numero: "))
resultado = 0


print("\nEl numero que escogio es:",num, "\nEl segundo nombre es:",num2)

opcion = input("""
                Ingrese el numero de la operación que desea:
                1. Sumar
                2. Restar
                3. Multiplicar
                4. Dividir
                Opcion: """)

#Para sumar
if opcion == "1":
    resultado = num + num2
    print(resultado)

#Para restar
elif opcion == "2":
    resultado = num - num2
    print(resultado)

#Para multiplicar
elif opcion == "3":
    resultado = num * num2
    print(resultado)

#Para dividir 
elif opcion == "4":
    resultado = num / num2
    print(resultado)
    
else:
    print("No escogieste un numero")
    
