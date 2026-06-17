def load_menu_items(filename:str)-> dict:
    #Open menu.txt: create a file handler to open file and read mode
    data_file = open(filename,"r")
    print(data_file)
    #Create an empy dictionary
    menu_items = {}
    #Use a loop to read the contents of the file line by line
    for line_of_data in data_file:
        #Split the line at the comma
        item_name_and_price = line_of_data.split(",")
        print(item_name_and_price)
        #Get the item adn price fromt eh list
        item_name = item_name_and_price[0]
        item_price = float(item_name_and_price[1])
        #Create and entry in the dicitionary fro the item and price
        menu_items[item_name] = item_price
    #Close the file
    data_file.close

    #print all entris from the dicotnary
    return menu_items
    






def main():
    # Define the menu items in a dictionary

    menu_items = load_menu_items("menu.txt")



    #Print the menu
    for item  in menu_items:
        print(f"{item}: ${menu_items[item]:.2f}")

    #Prompt the user

    total = 0
    
    
    while True:
        try:
            order = input("Item:\n").title()
            if order in menu_items.keys() :
                total += menu_items[order]
                print(f"Total: ${total:.2f} ")
            if order.lower() == "end":
                break
        except:
            continue

main()