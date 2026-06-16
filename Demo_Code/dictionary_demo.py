def main():
    # The need for dictionaries
    scores = [55,75,87,82,91]
    students = ["Alice","Bob","Jerry","Jane","Bill"]

    # Print the names of the students with their scores
    print("Students and scores using the lists\n----------------------------")

    for index in range(len(scores)):
        print(f"{students[index]}:{scores[index]}")

    # Create a dictonary of names and scores
    student_scores = {
        "Alice":55,
        "Bob":75,
        "Jerry":87,
        "Jane":82,
        "Bill":91
    }
    #print bob and janes scores

    print("\n Print Bob and Janes Scores\n---------------------")
    print(student_scores["Bob"])
    print(student_scores["Jane"])

    # Print all the data ion the student scores dictonary

    for student in student_scores:
        print(f"{student} : {student_scores[student]}")


    #create a dicitionary to store care information
    # make,model,year,value,engine size
    car_1 = {"make" : "Ferrari","model":"F-50","year":2024,"value":500000,"engine size": 4.8}

    print("\nGet all Car info\n-----------------------")

    for key, value in car_1.items():
        print(f"{key}: {value}")
    
    # create a second car
    car_2 = {"make" : "Honda","model":"Accord","year":2024,"value":18000,"engine size": 2.4}
    car_1["transmission"] = "manual"
    car_2["transmission"] = "automatic"
    # create a list of dictonaries
    dictionary_list = [car_1,car_2]

    # Display information for all cars

    print("\n Display information for all cars\n----------------------")

    # loop over all the cars

    for car in dictionary_list:
        print("\n Car Information\n---------------------")

        for feature, value in car.items():
            print(f"{feature}: {value}")

    #Create a dictonary of dicotnaries
    car_dictonary = {"Ferrari":car_1,"Honda":car_2}


    #Print all car information from teh dictonary
    print("\nCar info from dictonaries\n--------------------------------")

    for make, car in car_dictonary.items():
        print(f"\n{make}\n---------------")
        for feature, value in car.items():
            print(f"{feature}: {value}")
    # Getting a value from a dictonary when no key exists
    key = "model"
    car_1.keys()
    print("Finding key using Try/Except\n-------------------")
    try:
        print(f"{car_1[key]}")
    except:
        print(f"Error: Key {key} does not exist in the dictonary")
    print("\nFinding key using Dictonary.keys()\n---------------")
    if key not in car_1.keys():
        print(f"Error: Key {key} does not exist in the dictonary")
    else:
        print(f"{car_1[key]}")

    #Add an entry to a dictionary
    



main()