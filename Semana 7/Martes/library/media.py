class Media:
    def __init__(self, id):
        self.id = id

class Video(Media):
    def __init__(self, id, resolution):
        super().__init__(id)
        self.resolution = resolution

class Music(Media):
    def __init__(self, id, duration, gender):
        super().__init__(id)
        self.duration = duration
        self.gender = gender