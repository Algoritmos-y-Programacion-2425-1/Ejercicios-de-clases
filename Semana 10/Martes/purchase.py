class Purchase:
    def __init__(self, user, devices):
        self.user = user
        self.devices = devices

    def show_invoice(self):
        print("****** INVOICE ******")
        print(f"Name: {self.user.name}")
        print(f"Last Name: {self.user.lastname}")
        print(f"DNI: {self.user.dni}")
        amount = 0
        for index, device in enumerate(self.devices):
            print(f"id:{index + 1} - Model:{device.model} - Price:{device.price}")
            amount += device.price
        print(f"Amount: {amount}")

        