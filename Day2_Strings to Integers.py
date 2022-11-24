# Write a function called convert_add that takes a list of strings as an argument and converts it to integers and sums the list. 
# For example [‘1’, ‘3’, ‘5’] should be converted to [1, 3, 5] and summed to 9.

def convert_add (list_string):
    total_number = 0
    for i in numbers:
        total_number += int(i)
    return total_number


# Test
numbers = ['1', '3', '5']
print(f'The sum is {convert_add(numbers)}')





# Write a function called check_duplicates that takes a list of strings as an argument. The function should check if the list has any duplicates. If there are duplicates, the function should return
# the duplicates. If there are no duplicates, the function should return "No duplicates". For example, the list of fruits below should return apple as a duplicate and list of names should return "no duplicates".
fruits = ['apple', 'orange', 'banana', 'apple']
names = ['Yoda', 'Moses', 'Joshua', 'Mark']


def check_duplicates(string_list):
    holder_list = []
    for i in string_list:
        if i not in holder_list:
            holder_list.append(i)
        else:
            return i
    if string_list == holder_list:
        return 'No duplicates'


print(check_duplicates(names))
print(check_duplicates(fruits))


## OR 

def check_duplicates2(arr: list):
    for i in arr:
        if arr.count(i) > 1:
            return i
        else:
            return 'No duplicates'


print(check_duplicates2(names))
print(check_duplicates2(fruits))
