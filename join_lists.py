def join_lists():
    # Exercise 4.2 Lists into dictionaries, 5 Points

    # List of ingredients
    ingredient = ['Eggs', 'Flour', 'Milk', 'Butter', 'Cacao', 'Yeast', 'Soda', 'Backingpowder', 'GingerSpiceMix', 'Salt', 'Suggar']
    
    # List of corresponding amounts
    amount = [5, 2, 3, 500, 25, 1, 20, 15, 20, 50, 150]

    # Combine the two lists into a dictionary using zip
    myDict = dict(zip(ingredient, amount))

    # Return the dictionary
    return myDict