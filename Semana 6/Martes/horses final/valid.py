class Valid:
    def __init__(self, number, races):
        self.races = races
        self.number = number
    
    def start_valid(self):
        print(f"Arranca la valida numero {self.number}")
        for race in self.races:
            race.start_race()
