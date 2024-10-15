from horse import Horse

def main():
    horse = Horse("Rayo Veloz",1,"Blanco")
    horse.name = "Rayo McQueen"
    horse.set_number(2)
    print(horse.get_number())
    print(horse.name)

main()