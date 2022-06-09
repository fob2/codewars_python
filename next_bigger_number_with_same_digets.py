""" Create a function that takes a positive integer and returns the next bigger number
that can be formed by rearranging its digits. For example:

12 ==> 21
513 ==> 531
2017 ==> 2071
nextBigger(num: 12)   // returns 21
nextBigger(num: 513)  // returns 531
nextBigger(num: 2017) // returns 2071
If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift):

9 ==> -1
111 ==> -1
531 ==> -1
nextBigger(num: 9)   // returns nil
nextBigger(num: 111) // returns nil
nextBigger(num: 531) // returns nil 

My Solution:"""

from itertools import permutations

from itertools import permutations
  
def next_bigger(val):
    arr = [int(x) for x in list(str(val))]
    if len(arr) > 7:
        arr = [int(x) for x in list(str(val))]
        arr1 = arr[-8:]
        val1 = int(''.join([str(x) for x in arr1]))
        gen = permutations(arr1)
        arr2 = ([str(x) for x in y] for y in gen) 
        arr3 = (sorted(list(set([int(''.join(x)) for x in arr2]))))
        if len(arr3) <= 1:
            return -1
        elif len(arr3) > 1:
            if arr3.index(val1) <= len(arr3) - 2:
                arr4 = arr[:-8] + list(str(arr3[arr3.index(val1) + 1]))
                return int(''.join([str(x) for x in arr4]))
            else:
                return -1
        else:
            return -1
    else:
        a = permutations(arr)
        a1 = ([str(x) for x in y] for y in a) 
        a2 = (sorted(list(set([int(''.join(x)) for x in a1]))))
        if len(a2) <= 1:
            return -1
        elif len(a2) > 1:
            if a2.index(val) <= len(a2) - 2:
                return a2[a2.index(val) + 1]
            else:
                return -1
        else:
            return -1