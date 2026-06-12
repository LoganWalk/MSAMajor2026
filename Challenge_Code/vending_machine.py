

# Make a function that is the base function
# This function will start it off with displaying the name(Vending Machine) then seperate it with (-----------------)
# The name of this function will be vending_name






# Make a function called prompt_user
# This function will display the amount due 
# It will also check the amount to seee if it has hit 0 so when it does it will display Change Owed: 0
# This function will also have a while loop that stops when 50 cents or more is inserted 
# This function will subtract the amount inserted from the amount due only whne a valid coin is entered 


        








# Function check_amount_inserted will use a infinte while loop with try and except where it will ask the user to insert a coin 
# It will then check the coin to see if it is in the incremental of 1,5,10,25, if it is not then it will ask the user to insert a coin agian and not chnage the amount due 
# Once the user inserts a valid coin it will return that value to prompt_user fun
    
                
                
# Function main will call function vending_name and function propmt_user
def main():
    print(f"Vending Machine\n-------------------------")
    amount_due = 50
    while(True):
        print(f"Amount due: {amount_due}")
        try:
            
            insert_coin = int(input(f"Insert Coin: "))
            if insert_coin == 1 :
                amount_due -= 1
                if amount_due <= 0:
                    change_owed = amount_due*-1
                    print(f"Change owed:{change_owed} ")
                    break
            
                
            
            if insert_coin == 5  :
                amount_due -= 5
                if amount_due <= 0:
                    change_owed = amount_due*-1
                    print(f"Change owed:{change_owed} ")
                    break
                
                
            
            if insert_coin == 10 :
                amount_due -= 10
                if amount_due <= 0:
                    change_owed = amount_due*-1
                    print(f"Change owed:{change_owed} ")
                    break
                
        
            
            if insert_coin == 25 :
                amount_due -= 25
            
                if amount_due <= 0:
                    change_owed = amount_due*-1
                    print(f"Change owed:{change_owed} ")
                    break
                


        except:
            print(f"Insert Coin: ")
            continue

main()