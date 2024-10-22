from specialRooms import Quirofano, Consultorio, SalasTerapia

class Hospital:
    def __init__(self, name, location, capacity, special_rooms):
        self.name = name
        self.location = location
        self.capacity = capacity
        self.special_rooms = special_rooms

    def mostrar(self):
        print(f"Nombre: {self.name}")
        for room in self.special_rooms:
            if isinstance(room,Quirofano):
                print("Quirofano:", room.identification)
            elif isinstance(room,Consultorio):
                print("Consultorio:",room.identification)
