from hospital import Hospital
from specialRooms import Quirofano, Consultorio

def main():
    special_rooms = [
        Quirofano(1, "Piso 1"),
        Consultorio(2,"Piso 2")
    ]
    hospital = Hospital(
        "El llanito",
        "Caracas",
        2000,
        special_rooms
    )
    hospital.mostrar()
main()