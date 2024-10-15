from horse import Horse
from race import Race
from valid import Valid

def create_races(horses,races,race_quantity):
    for index in range(race_quantity):
        races.append(Race(index+1,horses))

def create_valids(valids,races):
    valids.append(Valid(5,races))
    valids.append(Valid(6,races))

def create_horses(horses):
    horses.append(Horse("Rayo",1,"Blanco"))
    horses.append(Horse("Relampago",2,"Negro"))
    horses.append(Horse("Hugo",3,"Gris"))
    horses.append(Horse("Furia",4,"Marron"))
    horses.append(Horse("Apolo",5,"Negro"))
    horses.append(Horse("Diablo",6,"Rojo"))

def main():
    race_quantity = int(input("How many races do you want for each valid: "))
    horses = []
    races = []
    valids = []
    create_horses(horses)
    create_races(horses,races,race_quantity)
    create_valids(valids, races)
    for valid in valids:
        valid.start_valid()
main()