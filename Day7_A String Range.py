# Write a function called string_range that takes a single number and returns a string of its range. The string characters should be separated by dots(.) 
# For example, if you pass 6 as an argument, your function should return ‘0.1.2.3.4.5’.

def string_range(number):
    empty_string = ''
    for i in range(number):
        empty_string += str(i) + '.'
    return empty_string[:-1]


print(string_range(6))

    
# Extra Challenge: Dictionary of Names
# You are given a list of names, and you are asked to write a code that returns all the names that start with ‘S’. Your code should return a dictionary of all the names that start with S and how 
# many times they appear in the dictionary. Here is a list below:
names = ["Joseph","Nathan", "Sasha", "Kelly", "Muhammad", "Jabulani", "Sera", "Patel", "Sera"]
# Your code should return: {“Sasha”: 1, “Sera”: 2}

def dict_names(arr: list):
    s_names = {}
    # check if item from arr starts with "s"
    for name in arr:
        #     # check if item from list is in dictionary key
        if name.startswith("S") and name in s_names.keys():
            # increment by 1
            s_names[name] += 1
        elif name.startswith("S") and name not in s_names.keys():
            # add it 
            s_names[name] = 1
    return s_names


print(dict_names(names))


d = {} # Creating an empty dictionary
for name in names:
    if name.startswith('S'):
 # Using the dictionary update method
        d.update({name: names.count(name)})
print(d)

