amount_due = None


# Make a function that is the base function
# This function will start it off with displaying the name(Vending Machine) then seperate it with (-----------------)
# The name of this function will be vending_name
def vending_name():
    print(f"Vending Machine\n-------------------------")





# Make a function called prompt_user
# This function will display the amount due 
# It will also check the amount to seee if it has hit 0 so when it does it will display Change Owed: 0
# This function will also have a while loop that stops when 50 cents or more is inserted 
# This function will subtract the amount inserted from the amount due only whne a valid coin is entered 
def prompt_user():
    amount_due = 50
    while(amount_due > 0):
        print(f"Amount Due: {amount_due}")
        valid_amount = check_amount_inserted()

        amount_due = amount_due - valid_amount
    print("Change Owed: 0")

        








# Function check_amount_inserted will use a infinte while loop with try and except where it will ask the user to insert a coin 
# It will then check the coin to see if it is in the incremental of 1,5,10,25, if it is not then it will ask the user to insert a coin agian and not chnage the amount due 
# Once the user inserts a valid coin it will return that value to prompt_user function
def check_amount_inserted():
    amount_due = 50
    while(amount_due>0):
        try:
            print(f"Amount Due: {amount_due}")
            insert_coin = int(input(f"Insert Coin: "))
            if insert_coin != 1 or insert_coin != 5 or insert_coin != 10 or insert_coin != 25 :
                continue
            
            break
            
        except:
            continue
    return insert_coin








# Function main will call function vending_name and function propmt_user
def main():
    vending_name()
    prompt_user()

main()