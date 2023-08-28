def add_numbers():
    # Takes input for the first linked list
    list_1 = input(
        "Enter non-negative list of numbers(seperate with space) \n")
    # Takes input for the second linked list
    list_2 = input("Enter non-negative list of numbers(seperate with space \n")

    # splits input into individual elements in an array
    list1, list2 = list_1.split(), list_2.split()
    list1.reverse()
    list2.reverse()  # returns a reversed list

    # converts each element into a string,concatenates it and cast it into an int value
    combined_list1 = int(''.join(map(str, list1)))
    combined_list2 = int(''.join(map(str, list2)))

    Added_list = combined_list1 + combined_list2
    # Convert the result to a list of characters
    final_list = list(str(Added_list))
    final_list.reverse()  # Reverses the list in place
    print(final_list)


add_numbers()
