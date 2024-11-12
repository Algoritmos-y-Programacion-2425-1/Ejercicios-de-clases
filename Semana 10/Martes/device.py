class Device:
    def __init__(self, model, price):
        self.model = model
        self.price = price

class iPhone(Device):
    def __init__(self, model, price, storage):
        super().__init__(model, price)
        self.storage = storage

class AppleWatch(Device):
    def __init__(self, model, price, network):
        super().__init__(model, price)
        self.network = network