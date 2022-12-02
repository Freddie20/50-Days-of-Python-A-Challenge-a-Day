# DAY 13
# Write a function called your_vat. The function takes no parameter. The function asks the user to input the price of an item and VAT (vat should be a percentage). 
# The function should return the price of the item plus VAT. If the price is 220 and, VAT is 15% your code should return a vat inclusive price of 253.
# Make sure that your code can handle ValueError. Ensure the code runs until valid numbers are entered. (hint: Your code should include a while loop).

# def your_vat():
#     while True:
#         try:
#             former_price = int(input('What is the price of the item? '))
#             vat_charge = int(input("What is item's vat? "))
#         except ValueError:
#             print('Enter a valid number')
#         else:
#             new_price = ((former_price * vat_charge)/100) + former_price
#             return f'Your new price is {int(new_price)}'
        

# # Test
# print(your_vat())



# Extra Challenge: Pyramid of Snakes
# Write a function called Python_snakes that takes a number as an argument and creates the following shape, using the number’s range: (hint: Use the loops and emoji library. 
# If you pass 7 as argument, your code should print the following:

from emoji import emojize

def Python_snakes(arr: int):
    # the loop to determine the number of rows of the pyramid
    for i in range(0, arr):
        # The loop that determines number of columns
        for j in range(n, i, -1):
            # print space between the snake signs
            print(end=" ")
        for k in range(0, i):
            # printing the snake emoji
            print(emojize(':snake:'), end=" ")
    print("\n")


print(Python_snakes(7))
