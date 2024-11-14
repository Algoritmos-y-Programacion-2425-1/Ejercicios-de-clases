from customer import Customer
from insurance import HealthInsurancePolicy, VehicleInsurancePolicy, CustomerHealth
from sell import Sell

def register_customers(customer_list):
    customer_list.append(
        Customer(
            input("Please enter the customer name: "),
            input("Please enter the customer last name: "),
            input("Please enter the customer dni: "),
            input("Please enter the customer address: "),
            input("Please enter the customer phone: "),
            int(input("Please enter the customer age (numeric): "))
        )
    )
    option = input("Do you want to register another customer: Y - Yes / N - No: ")
    if option == "Y":
        register_customers(customer_list)

def show_customers(customer_list):
    for index, customer in enumerate(customer_list):
        print(f"id: {index} - Name: {customer.name} - {customer.last_name} - DNI: {customer.dni}")

def fill_customer_health(people, customer_list):
    show_customers(customer_list)
    customer_id = int(input("Please enter the person id for add to this policy: "))
    person = customer_list[customer_id]
    amount = 0
    if person.age < 10:
        amount = 20
    elif person.age < 20:
        amount = 30
    elif person.age < 40:
        amount = 50
    else:
        amount = 70
    people.append(
        CustomerHealth(
            person,
            amount
        )
    )
    option = input("Do you want to register another person for this policy: Y - Yes / N - No: ")
    if option == "Y":
        fill_customer_health(people, customer_list)

def sell(customer_list, sell_list):
    show_customers(customer_list)
    customer_id = int(input("Please enter the customer id for selling: "))
    selected_customer = customer_list[customer_id]
    customer_policies = []
    while True:
        option = input("What Kind of insurance policy do you want to sell: 1 - Health / 2 - Vehicle / 3- Exit: ")
        if option == "1":
            people = []
            fill_customer_health(people, customer_list)
            total_amount = 0
            for person in people:
                total_amount += person.amount    
            customer_policies.append(
                HealthInsurancePolicy(
                    input("Please enter the policy number: "),
                    float(input("Please enter the policy insurance amount (numeric): ")),
                    input("Please enter the policy start_date: "),
                    input("Please enter the policy end_date: "),
                    people,
                    total_amount
                )
            )
        elif option == "2":
            vehicle_type = input("What type of vehicle do you want to sell: 1 - Motorbike / 2 - Car / 3 - Big Car: ")
            amount = 0
            if vehicle_type == "1":
                amount = 15
            elif vehicle_type == "2":
                amount = 20
            else:
                amount = 30
            customer_policies.append(
                VehicleInsurancePolicy(
                    input("Please enter the policy number: "),
                    float(input("Please enter the policy insurance amount (numeric): ")),
                    input("Please enter the policy start_date: "),
                    input("Please enter the policy end_date: "),
                    input("Please enter the policy brand: "),
                    input("Please enter the policy model: "),
                    input("Please enter the policy year: "),
                    input("Please enter the policy plate: "),
                    amount,
                )
            )
        elif option == "3":
            break
        else:
            print("Invalid option")

    sell_list.append(
        Sell(
            selected_customer,
            customer_policies
        )
    )
    final_option = input("Do you want to sell to another customer: Y - Yes / N - No: ")
    if final_option == "Y":
        sell(customer_list, sell_list)
    
        


def show_statistics(sell_list):
    pass


def main():
    print("***** Welcome to Apple Store *****")
    customer_list = []
    sell_list = []
    while True:
        option = input("Please enter a valid option: \n1-Register customers\n2-Sell\n3-Statistics\n4-Exit\n->")
        if option == "1":
            register_customers(customer_list)
        elif option == "3":
            sell(customer_list, sell_list)
        elif option == "4":
            show_statistics(sell_list)
        elif option == "5":
            print("Thank you!")
            break
        else:
            print("Please enter a valid option")
main()

main()