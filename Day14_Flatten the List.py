# Day 14
# Write a function called flat_list that takes one argument, a nested list. The function converts the nested list into a onedimension list. 
# For example [[2,4,5,6]] should return [2,4,5,6].

def flat_list(arr: list):
    result = []
    for sublist in arr:
        for number in sublist:
            result.append(number)
    return result

# Test
print(flat_list([[2,4,5,6]]))


# Extra Challenge: Teacher’s Salary
# A school has asked you to write a program that will calculate teachers' salaries. The program should ask the user to enter the teacher’s name, the number of periods taught 
# in a month, and the rate per period. The monthly salary is calculated by multiplying the number of periods by the monthly rate. The current monthly rate per period is $20. 
# If a teacher has more than 100 periods in a month, everything above 100 is overtime. Overtime is $25 per period. For example, if a teacher has taught 105 periods, 
# their monthly gross salary should be 2,125. Write a function called your_salary that calculates a teacher’s gross salary. The function should return the teacher’s name, 
# periods taught, and gross salary. Here is how you should format your output:
# Teacher: John Kelly, Periods: 105 Gross salary:2,125

def your_salary():
    name = input('What is your name? ')
    periods = int(input('What is the number of periods taught? '))
    rate = 20
    if periods > 100:
        extra = (periods - 100) * 25
        gross_salary = (100 * rate) + extra
    else:
        gross_salary = periods * rate
    return f'Teacher: {name} \nPeriods: {periods} \nGross salary: {gross_salary:,}'

# Test
print(your_salary())


