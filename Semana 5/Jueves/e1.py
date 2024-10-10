def calcular_posicion(path):
    position = [0,0]
    for direction in path:
        if direction.upper() == "N":
            position[0] += 1
        elif direction.upper() == "S":
            position[0] += -1
        elif direction.upper() == "E":
            position[1] += 1
        elif direction.upper() == "W":
            position[1] += -1
        if position == [0,0]:
            return True
def main():
    path = "NESWW"
    if len(path) < 1 or len(path) > 10**4:
        print("ERROR. ha iongresa una cantidad de direcciones no permitidas.")
    salida = calcular_posicion(path)
    print(salida)
main()

