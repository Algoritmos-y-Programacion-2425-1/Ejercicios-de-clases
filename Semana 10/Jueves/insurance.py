class InsurancePolicy:
    def __init__(self, number, kind, insurance_amount, start_date, end_date):
        self.number = number
        self.kind = kind
        self.insurance_amount = insurance_amount
        self.start_date = start_date
        self.end_date = end_date

class CustomerHealth:
    def __init__(self, customer, amount):
        self.customer = customer
        self.amount = amount

class HealthInsurancePolicy(InsurancePolicy):
    def __init__(self, number, insurance_amount, start_date, end_date, people, total_amount_to_charge):
        super().__init__(number, "Health", insurance_amount, start_date, end_date)
        self.people = people
        self.total_amount_to_charge = total_amount_to_charge

class VehicleInsurancePolicy(InsurancePolicy):
    def __init__(self, number, insurance_amount, start_date, end_date, brand, model, year, plate, total_amount_to_charge):
        super().__init__(number, "Vehicle", insurance_amount, start_date, end_date)
        self.brand = brand
        self.model = model 
        self.year = year 
        self.plate = plate
        self.total_amount_to_charge = total_amount_to_charge
