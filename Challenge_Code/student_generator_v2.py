from Student import Student

def value(file_name):
    # make a data handler
    data_file = open(file_name, "r")
    print(data_file)
    students = []

    # make a for loop to read the data line by line
    for line_of_data in data_file:
        #split the line at the comma
        split_data = line_of_data.split(",")
        try:
            kid = Student(split_data[0],split_data[1],split_data[2],float(split_data[3]),float(split_data[4]),split_data[5])
        except:
            continue
        students += [kid]
    
    #close the file
    data_file.close()
    return students
student = value("students.csv")

for kid in student:
    kid.print_data()

