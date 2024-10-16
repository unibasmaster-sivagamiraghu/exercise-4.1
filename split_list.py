def split_list():
    # Exercise 4.1 Lists, 5 Points.

    numbers_1 = [9, 31, 47, 8, 55, 7, 27, 67, 18, 2, 3, 7, 5, 54, 87, 11, 96, 60, 2, 91, 31, 21, 11, 34, 55, 92, 12, 51, 10, 32, 4, 53, 13, 27, 39, 87, 81, 69, 26, 19, 52, 31, 16, 87, 41, 39, 47, 2, 69, 91, 47, 76, 69, 48, 74, 51, 72, 49]

    numbers_2 = [31, 25, 88, 4, 5, 27, 97, 52, 74, 17, 94, 85, 22, 37, 25, 55, 23, 83, 70, 30, 51, 75, 80, 39, 15, 82, 63, 66, 46, 49, 74, 77, 71, 48, 6, 39, 72, 30, 19, 59, 75, 0]

    # Combine both lists into one in the same order
    combined_numbers = numbers_1 + numbers_2

    # Create lists to hold numbers based on remainder when divided by 3
    remainder_0 = []
    remainder_1 = []
    remainder_2 = []

    # Loop through each number in the combined list while maintaining the original order
    for number in combined_numbers:
        if number % 3 == 0:
            remainder_0.append(number)
        elif number % 3 == 1:
            remainder_1.append(number)
        else:
            remainder_2.append(number)

    # Return the lists in the original order of the numbers
    return (remainder_0, remainder_1, remainder_2)
    # Exercise 4.1 Lists, 5 Points.

    numbers_1 = [9, 31, 47, 8, 55, 7, 27, 67, 18, 2, 3, 7, 5, 54, 87, 11, 96, 60, 2, 91, 31, 21, 11, 34, 55, 92, 12, 51, 10, 32, 4, 53, 13, 27, 39, 87, 81, 69, 26, 19, 52, 31, 16, 87, 41, 39, 47, 2, 69, 91, 47, 76, 69, 48, 74, 51, 72, 49]
    numbers_2 = [31, 25, 88, 4, 5, 27, 97, 52, 74, 17, 94, 85, 22, 37, 25, 55, 23, 83, 70, 30, 51, 75, 80, 39, 15, 82, 63, 66, 46, 49, 74, 77, 71, 48, 6, 39, 72, 30, 19, 59, 75, 0]

    # Combine both lists into one
    combined_numbers = numbers_1 + numbers_2

    # Create lists to hold numbers based on remainder when divided by 3
    remainder_0 = []
    remainder_1 = []
    remainder_2 = []

    # Loop through each number in the combined list without sorting
    for number in combined_numbers:
        if number % 3 == 0:
            remainder_0.append(number)
        elif number % 3 == 1:
            remainder_1.append(number)
        else:
            remainder_2.append(number)

    # Return the lists in the original order of the numbers
    return (remainder_0, remainder_1, remainder_2)