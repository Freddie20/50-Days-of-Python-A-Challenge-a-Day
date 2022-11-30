# Day 11
# Write a function called equal_strings. The function takes two strings as arguments and compares them. If the strings are equal (if they have the same characters and have equal length), it
# should return True, if they are not, it should return False. For example, ‘love’ and ‘evol’ should return True.

def equal_strings(string1,string2):
    str1 = sorted(string1)
    str2 = sorted(string2)
    if str1 == str2:
        return True
    else:
        return False


print(equal_strings('love', 'evol'))





# Extra Challenge: Swap Values
# Write a function called swap_values. This function takes a list of numbers and swaps the first element with the last element.
# For example, if you pass [2, 4,67, 7] as a parameter, your function should return [7, 4, 67, 2].

def swap_values(arr:list):
    first_number = arr[0]
    arr[0] = arr[-1]
    arr[-1] = first_number
    return arr



print(swap_values([2, 4,67, 7]))
    
