print("***** WELCOME TO PIZZERIA BELLA NAPOLI ******")

pizza_type = input("Please enter what kind of pizza do you want: \n1-Vegetarian\n2-Non Vegetarian\n->")
ingredient_selected = ""
if pizza_type == "1":
    ingredient = input("Please enter what ingredient do you want: \n1-Pimiento\n2-Tofu\n->")
    if ingredient == "1":
        ingredient_selected = "Pimiento"
    else:
        ingredient_selected = "Tofu"
    print(f"Vegetarian Pizza with Tomate, Mozzarella and {ingredient_selected}")
else:
    ingredient = input("Please enter what ingredient do you want: \n1-Jamon\n2-Peperoni\n3->Salmon\n->")
    if ingredient == "1":
        ingredient_selected = "Jamon"
    elif ingredient == "2":
        ingredient_selected = "Peperoni"
    else:
        ingredient_selected = "Salmon"
    print(f"Vegetarian Pizza with Tomate, Mozzarella and {ingredient_selected}")