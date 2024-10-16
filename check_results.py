# Run python check_results.py to check the results of your exercise



def exercise_1():
    from test import split_list_test
    print("-----------------------------")
    print("Testing Exercise 1: Lists")
    print("-----------------------------")
    try:
        split_list_test.test_function1()
    except Exception as e:
        print(f"An error occurred: {e}")
    print("-----------------------------")


def exercise_2():
    from test import join_lists_test
    print("-----------------------------")
    print("Testing Exercise 2: Lists into dictionaries")
    print("-----------------------------")
    try:
        join_lists_test.test_function1()
    except Exception as e:
        print(f"An error occurred: {e}")
    print("-----------------------------")


def exercise_3():
    from test import shopping_lists_test
    print("-----------------------------")
    print("Testing Exercise 3: Shopping lists")
    print("-----------------------------")
    try:
        shopping_lists_test.test_function1()
    except Exception as e:
        print(f"An error occurred: {e}")


def exercise_4():
    from test import de_tuple_test
    print("-----------------------------")
    print("Testing Exercise 4: Tuples")
    print("-----------------------------")
    try:
        de_tuple_test.test_function1()
    except Exception as e:
        print(f"An error occurred: {e}")
    print("-----------------------------")



if __name__ == "__main__":
    exercise_1()
    exercise_2()
    exercise_3()
    exercise_4()
