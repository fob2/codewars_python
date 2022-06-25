""" An Arithmetic Progression is defined as one in which there is a constant difference 
between the consecutive terms of a given series of numbers. You are provided with 
consecutive elements of an Arithmetic Progression. There is however one hitch: exactly 
one term from the original series is missing from the set of numbers which have been given 
to you. The rest of the given series is the same as the original AP. Find the missing term.

You have to write a function that receives a list, list size will always be at least 3 
numbers. The missing term will never be the first or last one.

Example
find_missing([1, 3, 5, 9, 11]) == 7 """

def find_missing(sequence):
    val1 = sequence[1] - sequence[0]
    val2 = sequence[2] - sequence[1]
    val3 = sequence[3] - sequence[2]
    if val1 == val2:
        gap = val1
    elif val1 == val3:
        gap = val1
    elif val2 == val3:
        gap = val2
    set1 = set(sequence)
    set2 = set(range(sequence[0], sequence[-1]+ 1, gap))
    return (set2 - set1).pop()