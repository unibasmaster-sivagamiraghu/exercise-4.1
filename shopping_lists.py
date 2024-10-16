def shopping_list(ingredients):
    # Exercise 4.3 Shopping list, 5 Points
    
    # Recipe for gingerbread
    gingerbread = { 
        'Milk': 0.2, 
        'Cream': 0.2, 
        'Suggar': 250, 
        'GingerSpiceMix': 4, 
        'Salt': 1, 
        'Cacao': 3, 
        'Flour': 350, 
        'Backingpowder': 1 
    }

    # Initialize the shopping list
    shopping = {}

    # Loop through each item in the gingerbread recipe
    for item, required_amount in gingerbread.items():
        # If the ingredient is in the provided ingredients and the available amount is less than required
        if item in ingredients:
            available_amount = ingredients[item]
            if available_amount < required_amount:
                # Add the difference to the shopping list
                shopping[item] = required_amount - available_amount
        else:
            # If the ingredient is not in the provided ingredients, add the full required amount to the shopping list
            shopping[item] = required_amount

    return shopping