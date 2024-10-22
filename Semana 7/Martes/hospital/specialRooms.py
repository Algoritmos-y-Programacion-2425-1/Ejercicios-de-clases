class SpecialRoom:
    def __init__(self, identification, location, inventory):
        self.identification = identification
        self.location = location
        self.inventory = inventory

class Quirofano(SpecialRoom):
    def __init__(self, identification, location):
        super().__init__(identification, location, "Bisturi, camilla y lamparas")

class SalasTerapia(SpecialRoom):
    def __init__(self, identification, location):
        super().__init__(identification, location, "Camilla, Balones medicinales")

class Consultorio(SpecialRoom):
    def __init__(self, identification, location):
        super().__init__(identification, location, "Escritorio. silla y camilla")
        