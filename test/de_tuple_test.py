import sys
import os

# Get the current script's directory
script_dir = os.path.dirname(os.path.realpath(__file__))

# Compute the path to the parent directory and add it to sys.path
parent_dir = os.path.abspath(os.path.join(script_dir, '..'))
sys.path.append(parent_dir)


import de_tuple

def test_function1():
    if de_tuple.de_tuple() == ["Orange", 10, 20, 30, 5, 15, 25]:
        print("Test passed")
        assert True
    else:   
        print("Test failed")
        print("Expected: ['Orange', 10, 20, 30, 5, 15, 25]")
        print(f"Got: {de_tuple.de_tuple()}")
        assert False

