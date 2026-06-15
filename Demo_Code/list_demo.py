def main():
    # Create a list of strings,integers, and different values
    names = ["John", "Mary", "Alice", "Bob"]
    list_of_integers = [10, 16, 24, 42, 14, 9]
    random_type_list = ["Cyd", 15, 22.3, True, "Frank"]
    empty_list = []


    # Print a list
    print(list_of_integers)

    # Add values to a list
    print("\nAdding Values to a List\n--------------------------------")
    names.append("Johnny")
    list_of_integers.append(63)
    list_of_integers.append(5)
    print(f"List of integers: {list_of_integers}")
    print(f"List of names: {names}")


    print("\nGet the number of items in a list\n----------------------------")
    print(f"items in Integer list: {len(list_of_integers)}")
    print(f"items in Names list: {len(names)}")
    print(f"items in Empty list: {len(empty_list)}")

    
    print(f"Get specific vales at the indexes in a list\n----------------------")
    print(f"First item in list: {names[0]}")
    print(f"Fourth item in list: {names[3]}")

    # Print all items in a list
    print("\n Printing all names\n-------------------")
    for name in names:
        print(name)
    print("\nPrinting all names with index values\n------------------------")
    for index in range(len(names)):
        print(f"names [{index + 1}] = {names[index]}")
    
    # Calculate the summ of all values in a list
    sum = 0
    for number in list_of_integers:
        sum += number
    print(f"Total: {sum}")

    # Calculate the average of all integers in list

    avg_of_all_integers = sum / len(list_of_integers)

    print(f"Average of all integers: {avg_of_all_integers:.2f}")

    # Does the list contian a specific item
    search_name = "Veronica"
    if(search_name not in names):
        print(f"{search_name} is not in the names list")
    if(search_name in names):
        print(f"{search_name} is in the names list")
    # Find the largest value in the list
    max_value = list_of_integers[0]
    min_value = list_of_integers[0]
    for number in list_of_integers:
        if(number > max_value):
            max_value = number
        if(number < min_value):
            min_value = number
    print(f"The max value in the list is: {max_value}")
    print(f"The min value in the list is: {min_value}")
        

main()