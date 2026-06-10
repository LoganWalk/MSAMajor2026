# Declare varaibles for global acsess
days_working_every_year = 350




# Ask the user for the hours and hourly wage and make sure they are valid answers 
def get_hours_worked():
    
    while True:
        try:
        # Prompt user to enter weight in lbs
            answer_1 = float(input("Enter numbers of hours worked daily: "))
        # if weight is less than or equal to 0 output error message amd reprompt the user
            if(answer_1 > 24 or answer_1 <= 0):
                print("Error: Need to enter number of hours less than 24 and greater than 0")
                continue
            break
        
        except:
            print("ERROR: Please enter only a number.\n")
        continue
    return answer_1
def get_hourly_wage():
    
    while True:
        try:
        # Prompt user to enter weight in lbs
            answer_2 = float(input("Enter the hourly wage: "))
        # if weight is less than or equal to 0 output error message amd reprompt the user
            if(answer_2 <= 0 ):
                print("Error: Need to enter number greater than 0")
                continue
            break
        
        except:
            print("ERROR: Please enter only a number.\n")
        continue
    return answer_2

def main():
    hours_worked = get_hours_worked()
    hourly_wage = get_hourly_wage()
    wages_before_tax = hours_worked * hourly_wage * days_working_every_year
    tax_amount = wages_before_tax * 0.12
    wages_after_tax = wages_before_tax - tax_amount

    print(f"Pay Advice\n------------------------")
    print(f"Hours Worked: {hours_worked}")
    print(f"Hourly Wage: ${hourly_wage}")
    print(f"Wages Before Taxes: ${wages_before_tax:.2f}")
    print(f"Tax Amount: ${tax_amount:.2f}")
    print(f"Wages After Tax: ${wages_after_tax:.2f}")




main()


    
    



