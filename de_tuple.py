def de_tuple():
    # Exercise 4.4 De_tuple, 5 Points
    
    # Given tuple
    tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
    
    # Create an empty list
    myList = []
    
    # Extracting elements from the tuple and appending them to the list
    myList.append(tuple1[0])  # Extracting the string "Orange"
    myList.extend(tuple1[1])  # Extending the list with [10, 20, 30]
    myList.extend(tuple1[2])  # Extending the list with (5, 15, 25)
    
    # Return the final list
    return myList