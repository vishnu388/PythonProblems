"""
date = '21/04/2021'
modified_date = '22/04/2021'
author = 'Vishnu'
description = ' A library for reading in 2D arrays of integers, doubles, or booleans from standard input and printing them out to standard output.'
"""
def PrintArray(R, C):
    a1 = []
    print("Enter the entries row wise:")

    # For user input
    for i in range(R):  # A for loop for row entries
        a2 = []
        for j in range(C):  # A for loop for column entries
            a2.append(input())
        a1.append(a2)

    # For printing the array
    for i in range(R):
        for j in range(C):
            print(a1[i][j], end=" ")
        print()
try:
    PrintArray(3, 3)
except Exception as e:
    print(e)