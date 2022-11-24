# DAY 5
# Create a function called my_discount. The function takes no arguments but asks the user to input the price and the discount (percentage) of the product. Once the user inputs the price and discount, 
# it calculates the price after the discount. The function should return the price after the discount. For example, if the user enters 150 as price and 15% as the discount, your function should return 127.5.

def my_discount():
    previous_price = float(input('what is the price? '))
    discount = float(input('what is the discount? '))
    discount = 100/discount
    discount_value = previous_price/discount
    new_price = previous_price - discount_value
    return f'Your new price is {new_price}'

# Test
print(my_discount())


# Extra Challenge: Tuple of Student Sex
# You work for a school and your boss wants to know how many female and male students are enrolled in the school. The school has saved the students in a list. Your task is to write a code that will count 
# how many males and females are in the list. Here is a list below:
students = ['Male', 'Female', 'female', 'male', 'male', 'male','female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']
#Your code should return a list of tuples. The list above should return:
# [(‘Male’,7), (‘female’,6)]

def gender_count(arr: list):
    lowercase_list = []
    gendercount_list = []
    for gender in arr:
        lowercase_list.append(gender.lower())
    for sex in lowercase_list:
        if sex[0].startswith('m'):
            gendercount_list.append((sex, lowercase_list.count(sex)))
            break
    for f_sex in lowercase_list:
        if f_sex[0].startswith('f'):
            gendercount_list.append((f_sex, lowercase_list.count(f_sex)))
            break
    return gendercount_list


# Test
print(gender_count(students))




        


