# Day 9
# Create a function called biggest_odd that takes a string of numbers and returns the biggest odd number in the list. For example, if you pass ‘23569’ as an argument, your function should return 9. 
# Use list comprehension.


# def biggest_odd(arr:str):
#     string = [string for string in arr if int(string) % 2 != 0]
#     return max(string)


# print(biggest_odd('23569'))



# Extra Challenge: Zeros to the End
# Write a function called zeros_last. This function takes a list as argument. If a list has zeros (0), it will move them to the front of the list and maintain the order of the other numbers in the list.
# If there are no Zeros in the list, the function should return the original list sorted in ascending order. 
# For example, if you pass [1, 4, 6, 0, 7,0,9] as an argument, your code should return [1, 4, 6, 7, 9, 0, 0]. If you pass [2, 1, 4, 7, 6] as your argument, your code should return [1, 2, 4, 6, 7].


def zeros_last(arr: list):
    i = 0 # setting index 0
    arr1 = arr
    for num in arr:
        # Checking for non-zero numbers
        if num != 0:
            # Moving non-zero numbers to the front of the list
            arr[i] = num
            i += 1

    # Moving zero elements to the end of the list.
    while i < len(arr):
        arr[i] = 0
        i += 1
        return arr
    else:
    # if no zeros return original list in ascending order
        return sorted(arr1)

list1 = [1, 4, 6, 0, 7, 0]
list2 = [2, 1, 4, 7, 6]
print(zeros_last(list1))
print(zeros_last(list2))