# Write a function called only_floats, which takes two parameters a and b, and returns 2 if both arguments are floats, returns 1 if only one argument is a float, and returns 0 if neither 
# argument is a float. If you pass (12.1, 23) as an argument, your function should return a 1

def only_floats(a ,b):
    if isinstance(a, float) and isinstance(b, float):
        return 2
    elif isinstance(a, float) or isinstance(b, float):
        return 1
    else:
        return 0


# Test
print(only_floats(12.1, 23))



# Write a function called word_index that takes one argument, a list of strings and returns the index of the longest word in the list. 
# If there is no longest word (if all the strings are of the same length), the function should return zero (0). For example, the list below should return 2.
words1 = ["Hate", "remorse", "vengeance"]
# And this list below, should return zero (0)
words2 = ["Love", "Hate"]


def word_index(arr: list):
    word_length = 0
    word_position = 0
    for word in arr:
        number_word = len(word)
        if number_word > word_length:
            word_length = number_word
            word_position = arr.index(word)
    return word_position


# Test
print(word_index(words1))
print(word_index(words2))



