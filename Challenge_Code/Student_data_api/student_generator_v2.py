from Student import Student

def load_students():
    # make a data handler
    data_file = open("students.csv", "r")
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


def student_to_dictionary(list_of_students: list[Student]) -> list[dict]:
    #create an empty list to store the dictionaries
    student_dictionary_list = []

    #loop through the list of students and write each students data to a dictionary
    for student in list_of_students:
        #create an empty dictionary
        student_dictionary = {}

        #make entries into the dictionary using the student properties
        #firstname, last name, major, gpa, class, id
        student_dictionary['first_name'] = student.get_first_name()
        student_dictionary['last_name'] = student.get_last_name()
        student_dictionary['major'] = student.get_major()
        student_dictionary['gpa'] = student.get_gpa()
        student_dictionary['class'] = student.get_class_level()
        student_dictionary['id'] = student.get_id()

        #append the dictionary to the list of dictionaries
        student_dictionary_list.append(student_dictionary)

    #return the list of dictionaries
    return student_dictionary_list

def get_student_dictionaries():
    student_list = load_students()

    #get a list of student dictionaries
    student_dictionaries = student_to_dictionary(student_list)

    return student_dictionaries



