import sys
import os

# Get the current script's directory
script_dir = os.path.dirname(os.path.realpath(__file__))

# Compute the path to the parent directory and add it to sys.path
parent_dir = os.path.abspath(os.path.join(script_dir, '..'))
sys.path.append(parent_dir)


import join_lists

def test_function1():
    myDict = join_lists.join_lists()

    expected_values = {
        'Eggs': 5,
        'Milk': 3,
        'Butter': 500,
        'Cacao': 25,
        'Yeast': 1,
        'Soda': 20,
        'Backingpowder': 15,
        'GingerSpiceMix': 20,
        'Salt': 50,
        'Suggar': 150
    }


    print(f"myDict: {myDict}")
    # Check if all values match
    if all(myDict[key] == expected_values[key] for key in expected_values):
        print("Test passed")
        assert True
    else:
        print("Test failed")
        for key in expected_values:
            if myDict[key] != expected_values[key]:
                print(f"Expected {key}: {expected_values[key]}, but got: {myDict[key]}")
        assert False
