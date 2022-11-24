# DAY 1

# Write a function called divide_or_square that takes one argument (a number), and returns the square root of the number if it is divisible by 5, returns its remainder if it is not divisible by 5
# For example, if you pass 10 as an argument, then your function should return 3.16 as the square root.

import math

def divide_or_square(value):
    if value % 5 == 0:
        return math.sqrt(value)
    else:
        return value % 5


# # Test

for i in range(0,26,5):
    print(divide_or_square(i))



# Write a function called longest_value that takes a dictionary as an argument and returns the first longest value of the dictionary. For example, the following dictionary should return – apple as the longest value.
# fruits = {'fruit': 'apple', 'color': 'green'}

def longest_value(dict_name):

    p_len= 0
    longest_string= ""

    for i in dict_name.keys():
        len_i = len(dict_name[i])

        if len_i > p_len:
            longest_string= dict_name[i]
            p_len= len_i
            print(longest_string)

    print("\n")
    
    return longest_string


## Test
fruits = {'fruit': 'apple', 'color': 'green', 'label': 'browny'}

print(longest_value(fruits))