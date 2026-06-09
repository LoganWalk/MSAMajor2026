# Programm to convert lbs to kg
# INPUT(getting the data the will be processed)

# Loop

while True:
    try:
        # Prompt user to enter weight in lbs
        user_weight = float(input("Enter weight in lbs: "))
        # if weight is less than or equal to 0 output error message amd reprompt the user
        if user_weight <= 0:
            print("ERROR: Enter a number greater than zero")
            continue
        break
        
    except:
        print("ERROR: Please enter only a number.\n")
    continue
    # Validate input ensure the is a number
    # If the input in invalid then reprompt the user until the input is valid

    


# PROCESSING
# Use a conversion factor to convert lbs to kgs(2.205 lbs = 1 kg)
lbs_to_kg = 2.205
user_weight_in_kg = user_weight / lbs_to_kg



#OUTPUT
# Print the output to the user

print(f"You weigh {user_weight_in_kg:.2f} kgs.")
