import sys
import os

# Get the current script's directory
script_dir = os.path.dirname(os.path.realpath(__file__))

# Compute the path to the parent directory and add it to sys.path
parent_dir = os.path.abspath(os.path.join(script_dir, '..'))
sys.path.append(parent_dir)



import split_list

def test_function1():
    remainder_0 = [0, 3, 6, 9, 12, 15, 18, 21, 27, 30, 39, 48, 51, 54, 60, 63, 66, 69, 72, 75, 81, 87, 96]
    remainder_1 = [4, 7, 10, 13, 16, 19, 22, 25, 31, 34, 37, 46, 49, 52, 55, 67, 70, 76, 82, 85, 88, 91, 94, 97]
    remainder_2 = [2, 5, 8, 11, 17, 23, 26, 32, 41, 47, 53, 59, 71, 74, 77, 80, 83, 92]
    rem0, rem1, rem2 = split_list.split_list()
    if (remainder_0 == rem0) and (remainder_1 == rem1) and (remainder_2 == rem2):
        print("Test passed")
        assert True
    else:
        print("Test failed")
        if remainder_0 != rem0:
            print(f"Expected remainder_0: {rem0}, but got: {remainder_0}")
        if remainder_1 != rem1:
            print(f"Expected remainder_1: {rem1}, but got: {remainder_1}")
        if remainder_2 != rem2:
            print(f"Expected remainder_2: {rem2}, but got: {remainder_2}")
        assert False

