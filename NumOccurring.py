"""-----------------------------------------------------------------------
Python3 program to find the element occurring odd and even number of times
-----------------------------------------------------------------------"""


import numpy as np


def Initialize(arr):        # Initialize the Dictionary or HashMap
    count = {}

    for num in arr:
        count[num] = count.get(num, 0) + 1

    return count


def CountOdd(arr):      # Function to count Odd occurrence
    count = Initialize(arr)

    for num in count:
        if count[num] % 2 != 0:
            print(num)


def CountEven(arr):     # Function to count Even occurrence
    count = Initialize(arr)

    for num in count:
        if count[num] % 2 == 0:
            print(num)


if __name__ == '__main__':
    try:
        array = np.array(list(map(int, input("Enter the Array: ").strip().split(' '))))

        CountOdd(array)
        CountEven(array)

    except Exception as e:
        print("Error: " + str(e))
