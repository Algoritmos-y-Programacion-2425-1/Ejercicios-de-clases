class Horse:
    def __init__(self, name, number, color):
        self.__number = number
        self.name = name
        self.color = color

    def get_number(self):
        return self.__number
    
    def set_number(self, number):
        self.__number = number