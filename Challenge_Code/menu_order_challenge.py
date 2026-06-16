def main():
    # Define the menu items in a dictionary

    menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00}

    #Print the menu
    for item  in menu:
        print(f"{item}: ${menu[item]:.2f}")

    #Prompt the user

    total = 0
    
    
    while True:
        try:
            order = input("Item:\n").title()
            if order in menu.keys() :
                total += menu[order]
                print(f"Total: ${total:.2f} ")
            if order.lower() == "end":
                break
        except:
            continue
    

    
    


    






































main()