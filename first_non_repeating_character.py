""" Write a function named first_non_repeating_letter that takes a string input, 
and returns the first character that is not repeated anywhere in the string.

For example, if given the input 'stress', the function should return 't', 
since the letter t only occurs once in the string, and occurs first in the string.

As an added challenge, upper- and lowercase letters are considered the same character, 
but the function should return the correct case for the initial letter. For example, 
the input 'sTreSS' should return 'T'.

If a string contains all repeating characters, it should return an empty string ("") 
or None -- see sample tests. 

My solution: """

def first_non_repeating_letter(string):
    if string == '':
        return ''
    else:
        li1 = [ord(x) for x in string]
        li2 = [ord(x) + 32 if ord(x) < 91 else ord(x) - 32 for x in string]
        li3 = [tuple(sorted(x)) for x in list(map(lambda x, y: (x,y), li1, li2))]
        li4 = [a for b in [x for x in li3 if li3.count(x) == 1] for a in b]
        if li4 == []:
            return ''
        else:
            return chr([x for x in li4 if x in li1][0])