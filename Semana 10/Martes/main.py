from device import iPhone, AppleWatch
from user import User
from purchase import Purchase

def register_devices(devices):
    while True:    
        option = input("Please enter the device type: \n1-iPhone\n2-Apple Watch\n3-Exit\n->")
        if option == "1":
            devices.append(
                iPhone(
                    input("Please enter the model: "),
                    float(input("Please enter the product price (numeric): ")),
                    input("Please enter the iPhone storage:")
                )
            )
        elif option == "2":
            network_option = input("Please enter the Apple Watch Network: 1-Wi-Fi or 2- Celular -> ")
            if network_option == "1":
                network_option = "Wi-Fi"
            else:
                network_option = "Celular"
            devices.append(
                AppleWatch(
                    input("Please enter the model: "),
                    float(input("Please enter the product price (numeric): ")),
                    network_option
                )
            )
        elif option == "3":
            break
        else:
            print("Please enter a valid option")

def register_users(users):
    users.append(
        User(
            input("Please enter the user name:"),
            input("Please enter the user last name:"),
            input("Please enter the user dni:")
        )
    )

def register_purchase(users, devices, purchases):
    print("Available Users:")
    for index, user in enumerate(users):
        print(f"id:{index} - Name: {user.name} {user.lastname} - DNI: {user.dni}")

    user_id = int(input("Please select the user id that you want: "))
    user_selected = users[user_id]
    user_devices = []
    for index, device in enumerate(devices):
        print(f"id:{index} - Model:{device.model} - Price:{device.price}")
    while True:
        device_id = int(input("Please enter the device id that you want, if you want to exit enter -1:"))
        if device_id == -1:
            break
        else:
            user_devices.append(
                devices[device_id]
            )
    purchase = Purchase(user_selected, user_devices)
    purchase.show_invoice()
    purchases.append(purchase)

def show_statistics(purchases):
    cont_iphone = 0
    cont_apple_watch = 0
    amount_iphone = 0 
    amount_apple_watch = 0
    apple_watch_wifi = 0
    apple_watch_celular = 0 
    for purchase in purchases:
        for device in purchase.devices:
            if isinstance(device, iPhone):
                cont_iphone += 1
                amount_iphone += device.price
            else:
                cont_apple_watch += 1
                amount_apple_watch += device.price
                if device.network == "Wi-Fi":
                    apple_watch_wifi += 1
                else:
                    apple_watch_celular += 1
    average = (amount_apple_watch+amount_iphone)/len(purchases)        
    print("The iPhone quantity is:", cont_iphone)
    print("The AppleWatch quantity is:", cont_apple_watch)
    print("The iPhone revenue is:", amount_iphone)
    print("The AppleWatch revenue is:", amount_apple_watch)
    print("The AppleWatch with Wifi is:", apple_watch_wifi)
    print("The AppleWatch with Celular is:", apple_watch_celular)
    print("The average by purchase is:", average )


    

def main():
    print("***** Welcome to Apple Store *****")
    device_list = []
    user_list = []
    purchase_list = []
    while True:
        option = input("Please enter a valid option: \n1-Register devices\n2-Register users\n3-Register Purchase\n4-Statistics\n5-Exit\n->")
        if option == "1":
            register_devices(device_list)
        elif option == "2":
            register_users(user_list)
        elif option == "3":
            register_purchase(user_list, device_list, purchase_list)
        elif option == "4":
            show_statistics(purchase_list)
        elif option == "5":
            print("Thank you!")
            break
        else:
            print("Please enter a valid option")
main()