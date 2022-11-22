# Write a function called register_check that checks how many students are in school. The function takes a dictionary as a parameter. If the student is in school, the dictionary says ‘yes’. If the student is not in school, the dictionary says ‘no’. Your 
# function should return the number of students in school. Use the dictionary below. Your function should return 3.


def  register_check(arr: dict):
    student_number = 0
    for item in arr:
        if arr[item] == 'yes':
            student_number += 1
    return student_number


register = {'Michael':'yes','John': 'no', 'Peter':'yes', 'Mary': 'yes'}

# Test
print(register_check(register))





names = ["kerry", "dickson", "John", "Mary", "carol", "Rose", "adam"]

# You are given a list of names above. This list is made up of names of lowercase and uppercase letters. Your task is to write a code that will return a tuple of all the names in the list that have only lowercase letters. Your tuple should have names sorted 
# alphabetically in descending order. Using the list above, your code should return:('kerry', 'dickson', 'carol', 'adam')
    
def lowercase_desc(arr: list):
    lowercase_tuple = ()
    for name in arr:
        if name[0].islower():
            print(name)
            lowercase_tuple= lowercase_tuple + (name, )
    lowercase_tuple = sorted(lowercase_tuple, reverse=True)
    return lowercase_tuple


# Test
print(lowercase_desc(names))