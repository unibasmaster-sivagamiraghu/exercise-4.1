import sys
import os

# Get the current script's directory
script_dir = os.path.dirname(os.path.realpath(__file__))

# Compute the path to the parent directory and add it to sys.path
parent_dir = os.path.abspath(os.path.join(script_dir, '..'))
sys.path.append(parent_dir)


import join_lists
import shopping_lists

def test_function1():
    inStock = join_lists.join_lists()
    shopping = shopping_lists.shopping_list(inStock)
    print(f"Got: {shopping}")
    if shopping['Cream'] == 0.2 and shopping['Suggar'] == 100 and shopping['Flour'] == 348:
        print("Test passed")
        assert True
    else:
        print("Test failed")
        print("Expected: {'Cream': 0.2, 'Suggar': 100, 'Flour': 348}")
        print(f"Got: {shopping}")
        assert False

