from Student import Student

def main():
    # make a data handler
    data_file = open("students.csv", "r")
    print(data_file)


    # make a for loop to read the data line by line
    for line_of_data in data_file:
        #split the line at the comma
        split_data = line_of_data.split(",")
        kid = Student(split_data[0],split_data[1],split_data[2],split_data[3],split_data[4],split_data[5])
        
        print(kid)
    #close the file
    data_file.close()


main()