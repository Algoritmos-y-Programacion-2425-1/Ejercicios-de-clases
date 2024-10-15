import random

class Race:
    def __init__(self, number, horses):
        self.number = number
        self.horses = horses

    def start_race(self):
        print("PARTIDAAAAAAAAAAAAAAAAAAAAAAAAAAAA!!!! Salieron los competidores!!!")
        print(f"Arranco la carrera {self.number}")
        self.choose_winner()

    def choose_winner(self):
        winner = random.choice(self.horses)
        print(f"El caballo ganador es: {winner.name}")