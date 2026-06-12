def main():
    my_name = "logan"

    # Capitalize a string
    print(f"My name capitalized: {my_name.capitalize()}");
    # Make a string uppercase
    print(f"My name uppercased: {my_name.upper()}")
    # Make a string lower case
    last_name = "Walk"
    print(f"my full name lowercased: {my_name.lower()} {last_name.lower()}")

    # compare two strings
    my_name_title_case = "Logan"
    if(my_name == my_name_title_case):
        print("The strings are equal")
    else:
        print("The strings are not equal")

    print("\nUsing the Startswith() Method\n---------------")
    # determine if a strng statrs with a set of characters
    print(f"{my_name} starts wit L or l: {my_name.startswith("L") or my_name.startswith("l")}")

    if(not my_name.startswith("Log") and (not my_name.startswith("log"))):
        print(f"You spelled {my_name} incorrectly")
    else:
        print(f"You spelled {my_name} correctly")
    if(not my_name.lower().startswith("log")):
        print(f"You spelled {my_name} incorrectly")
    else:
        print(f"You spelled {my_name} correctly")
    
    print("\n Using the Endswith() method \n-----------------")
    print(f"{my_name} ends with an : {my_name.endswith("an")}")

    print("\nUsing the find method \n -----------------")

    search_letter = "l"
    index_of_substring = my_name.find(search_letter)
    if(index_of_substring != -1):
        print(f"The {search_letter} is at index {index_of_substring} in {my_name}")

    print(f" The {search_letter} is at index {my_name.find(search_letter)} in {my_name}")


    print("Looping through a string\n-----------")
    for letter in my_name:
        print(letter)
    
    print(f"{my_name} has {len(my_name)}")
    # print the letters ina sting along ti=weith the index postions 
    for letter_index in range(len(my_name)):
        print(f"Letter {letter_index+1}: {my_name[letter_index]}")
    print("\nSearch a string \n------------------")
    sentence = "I have a dog. My dog is cute. Do you want a dog?"
    # Write code that counts the number of occurences of the word fo in the sentence
    # Expected outputs: 3
    search_word = "dog"
    start_index = 0
    number_of_dogs = 0
    while True:
        # start at the beginnign at the string
        # we are going to search for the occurence of the word dog starting at index 0
        dog_index = sentence.find(search_word,start_index)
        #if we find dog add 1 to some variable we use to keep track fo teh number of dogs we find
        # Continue searching for the string from the next index after the dog we just found
        # update teh starting index by 1
        if(dog_index == -1):
            break
        else:
            # number fo dogs is equal to numbers of dogs plus 1
            number_of_dogs += 1
            start_index = dog_index+1
        # do this until we dont find anymore dogs: when find() returns -1
    print(f"There are {number_of_dogs} {search_word}(s) in the sentence.")




    

main()