def main():
#While loop
    while True:
        
    # Input
    # Prompt the user
        expression = input("enter your expression(X Y Z): ")


    #Process
    #Validate the expression format
        #use the split method to split the expression at the space
        split_expression = expression.split(" ")
        #if the length of the resulting list is not 3 then invalid format
        if(len(split_expression) != 3):
            print("Invalid Format")
            continue
    #Validate that X and Z are integers
        #convert to int.
        try:
            x = int(split_expression[0])
            z = int(split_expression[2])
        except:
            print("Invalid Format: x and Z have to be integers")
            continue
        #If converting causes an exception then incorrect or invalid format
    #Validate that Y is an acceptable operator (+,-,*,/)
        y = split_expression[1]
        # use an if statement to determine if Y equals a valid operator
        valid_operators = ["+", "-", "*", "/"]
        if y not in valid_operators:
            print("Invalid Format: Operator not right")
            continue


        #invalid format if not
    # Validate that when Y is / Z is not 0
        if(y == "/" and z == "0"):
            print("Invalid Format: Divide by Zero Error")
            continue
        # use If: y == "/" and Z == 0: invalid format, divide by zero error
    #Do the math
        if(y == "+"):
            result = x + z
        if(y == "-"):
            result = x - z
        if(y == "*"):
            result = x * z
        if(y == "/"):
            result = x / z



        #OUTPUT
        #Print the answer
        print(f"Your answer is: {result:.1f}")
        # ask to do it again
        do_again = input("Press y if you want to go again, fi you dont want to go again then press 0: ")
        if(do_again == "y"):
            continue
        if(do_again == "0"):
            break




main()
