""" If we were to set up a Tic-Tac-Toe game, we would want to know whether the board's 
current state is solved, wouldn't we? Our goal is to create a function that will check 
that for us!

Assume that the board comes in the form of a 3x3 array, where the value is 0 if a spot
is empty, 1 if it is an "X", or 2 if it is an "O", like so:

[[0, 0, 1],
 [0, 1, 2],
 [2, 1, 0]]
We want our function to return:

-1 if the board is not yet finished AND no one has won yet (there are empty spots),
1 if "X" won,
2 if "O" won,
0 if it's a cat's game (i.e. a draw).
You may assume that the board passed in is valid in the context of a game of Tic-Tac-Toe. """

from itertools import chain

def is_solved(board):
    arr = list(chain.from_iterable(board))
    if arr[0] == arr[1] == arr[2] == 1 or arr[6] == arr[7] == arr[8] == 1 or arr[0] == arr[3] == arr[6] == 1 or arr[2] == arr[5] == arr[8] == 1:
        return 1
    elif arr[0] == arr[1] == arr[2] == 2 or arr[6] == arr[7] == arr[8] == 2 or arr[0] == arr[3] == arr[6] == 2 or arr[2] == arr[5] == arr[8] == 2:
        return 2
    elif arr[4] == 1:
        if arr[0] & arr[8] == 1 or arr[1] & arr[7] == 1 or arr[2] & arr[6] == 1 or arr[3] & arr[5] == 1:
            return 1
        elif 0 in arr:
            return -1
        else:
            return 0
    elif arr[4] == 2:
        if arr[0] & arr[8] == 2 or arr[1] & arr[7] == 2 or arr[2] & arr[6] == 2 or arr[3] & arr[5] == 2:
            return  2
        elif 0 in arr:
            return -1
        else:
            return 0
    else:
        return -1