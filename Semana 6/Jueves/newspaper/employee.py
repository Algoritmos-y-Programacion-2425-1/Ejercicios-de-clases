class Employee:
    def __init__(self, name, dni):
        self.name = name
        self.dni = dni

class Boss(Employee):
    def __init__(self, name, dni, writers):
        super().__init__(name, dni)
        self.writers = writers

    def supervise(self):
        print("Supervising my writters:")
        for writer in self.writers:
            print(writer.name)
            writer.write_article()
    
    def choice_article(self, list_articles):
        pass

class Writter(Employee):
    def __init__(self, name, dni):
        super().__init__(name, dni)

    def write_article(self):
        print("Writing...!")
