# Day 6
# Write a function called user_name that generates a username from the user’s email. The code should ask the user to input an email and the code should return everything before the @ sign as their user name. 
# For example, if someone enters ben@gmail.com, the code should return ben as their username.

def user_name():
    email_address = input('Input an email address ')
    user_email = email_address.split('@')
    return user_email[0]

# Test
print(user_name())



# Extra Challenge: Zero Both Ends
# Write a function called zeroed code that takes a list of numbers as an argument. The code should zero (0) the first and the last number in the list. 
# For example, if the input is [2, 5, 7, 8, 9], your code should return [0, 5, 7, 8, 0]

def zeroed_code(arr: list):
    arr[0] = 0
    arr[-1] = 0
    return arr


# Test
print(zeroed_code([2, 5, 7, 8, 9]))
