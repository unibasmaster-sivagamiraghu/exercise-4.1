# Exercise 04
Exercise for lists, sets, tuples, dictionaries, modules and classes

__Remark__: Hand-in via GitHub Classroom, Deadline 23.10.2024


You can test your solutions by running the following command:
```bash
python check_results.py
```
Please make sure that you `push` your solution when you are done with the exercise.


## Exercise 4.1: Lists, 5 Points

In the file `split_list.py` you find two given lists with numbers.

```python
numbers_1 = [
     9, 31, 47,  8, 55,  7, 27, 67, 18,  2, 
     3,  7,  5, 54, 87, 11, 96, 60,  2, 91, 
    31, 21, 11, 34, 55, 92, 12, 51, 10, 32, 
     4, 53, 13, 27, 39, 87, 81, 69, 26, 19, 
    52, 31, 16, 87, 41, 39, 47,  2, 69, 91, 
    47, 76, 69, 48, 74, 51, 72, 49
]
numbers_2 = [
    31, 25, 88,  4,  5, 27, 97, 52, 74, 17, 
    94, 85, 22, 37, 25, 55, 23, 83, 70, 30, 
    51, 75, 80, 39, 15, 82, 63, 66, 46, 49, 
    74, 77, 71, 48,  6, 39, 72, 30, 19, 59, 
    75, 0
]
```


Concatenate this list into one single list (called `numbers_1_2`) 
and remove all duplicates from the list.

Then split this list into 3 smaller lists called: 
```remainder_0, remainder_1, remainder_2```
* In the list `remainder_0` there should be all numbers whose modulus 3 equals 0 i.e. 
these numbers are a multiple of 3. 
* `remainder_1` should contain all the numbers whose modulus 3 equals 1.
* `remainder_2` all the numbers whose modulus 3 yields 2.

Sort the numbers in each of the three lists (`remainder_0`, `remainder_1`, and `remainder_2`)
 in ascending order and return the resulting lists all at once as 
```python
return(remainder_0, remainder_1, remainder_2)
```


## Exercise 4.2: Lists into dictionaries, 5 Points

Steve cataloged the contencts of his backing ingredients in his kitchen as two lists. The first listing the name of the ingredients and the second list gives the available amount of the respective ingredient (in the usual units):

```python
ingredient = ['Eggs', 'Flour', 'Milk', 'Butter', 'Cacao', 'Yeast', 'Soda', 'Backingpowder', 'GingerSpiceMix', 'Salt', 'Suggar']
amount     = [ 5,      2,       3,      500,      25,      1,       20,     15,              20,               50,     150    ]
```

Amend the Python function in `join_lists.py` that combines the two lists into on single dictionary whereas the ingredient is the `key` and `amount` the value of the entries.

Return this dictionary.


## Exercise 4.3: Shopping list, 5 Points

As the cold season is approaching fast, Steve would like to bake some Gingerbread (Lebkuchen). From Exercise 4.2 we already know the ingredients Steve has in his kitchen.

```python
gingerbread = { 
    'Milk':0.2, 
    'Cream':0.2, 
    'Suggar':250, 
    'GingerSpiceMix':4,     
    'Salt':1, 
    'Cacao':3, 
    'Flour':350, 
    'Backingpowder':1 
    }
````

Write a function `shopping_list.py` that gives back the shopping list as a Dictionary with the amount of each ingredient missing to bake the gingerbread. Only list those ingredients that Steve has to buy.


## Exercise 4.4: Tuples, 5 Points

Write a Python function `de_tuple.py` that converts the tuple below into a simple list.

```
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
```

and return the resulting list.

> 💡 **Tip:** The expected output list is: 
> ` ["Orange", 10, 20, 30, 5, 15, 25] `
