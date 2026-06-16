def main():
    #Open menu.txt: create a file handler to open file and read mode
    data_file = open("menu.txt","r")
    print(data_file)
    #Create an empy dictionary
    menu_items = {}
    #Use a loop to read the contents of the file line by line
    for line_of_data in data_file:
        #Split the line at the comma
        item_name_and_price = line_of_data.split(",")
        print(item_name_and_price)
        #Get the item adn price fromt eh list
        #Create and entry in the dicitionary fro the item and price
    #Close the file

main()