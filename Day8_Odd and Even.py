# Day 8
# Write a function called odd_even that has one parameter and takes a list of numbers as an argument. The function returns the difference between the largest even number in the list and 
# the smallest odd number in the list. For example, if you pass [1,2,4,6] as an argument the function should return 6 -1= 5.

def odd_even(arr: list):
    even = []
    odd = []
    for number in arr:
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)
    difference = max(even) - min(odd)
    return difference


# Test
print(odd_even([1,2,4,6]))


# Extra Challenge: List of Prime Numbers
# Write a function called prime_numbers. This function asks a user to enter a number (integer) as an argument and returns a list of all the prime numbers within its range. 
# For example, if user enters 10, your code should return [2, 3, 5, 7] as prime numbers.

def prime_numbers():
    prime_within = []
    int_number = int(input('Enter an interger number '))
    for number in range(int_number):
        if number != 1 and number % 2 != 0 and number % 3 != 0 and number % 5 != 0:
            prime_within.append(number)
        elif number == 2 or number == 3 or number == 5:
            prime_within.append(number)
    return prime_within

# Test
print(prime_numbers())