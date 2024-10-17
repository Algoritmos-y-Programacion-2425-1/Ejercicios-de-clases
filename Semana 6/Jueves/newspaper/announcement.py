class CommercialAnnouncement:
    def __init__(self, name, dni, section, title, body):
        self.name = name
        self.dni = dni
        self.section = section
        self.title = title
        self.body = body

class ClassifiedAnnouncement:
    def __init__(self, price, publish_date, days_quantity):
        self.price = price
        self.publish_date = publish_date
        self.days_quantity = days_quantity

class ClassifiedVehicleAnnouncement(ClassifiedAnnouncement):
    def __init__(self, price, publish_date, days_quantity, year, brand, model, color, km):
        super().__init__(price, publish_date, days_quantity)
        self.year = year
        self.brand = brand
        self.model = model
        self.color = color
        self.km = km

class ClassifiedHomeAnnouncement(ClassifiedAnnouncement):
    def __init__(self, price, publish_date, days_quantity, m2, rooms, bathrooms, parking_spaces, home_policy):
        super().__init__(price, publish_date, days_quantity)
        self.m2 = m2
        self.rooms = rooms
        self.bathrooms = bathrooms
        self.parking_spaces = parking_spaces
        self.home_policy = home_policy
