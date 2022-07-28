"""---------------------------------------------------
Program to do Union and Intersection between Two array
---------------------------------------------------"""


import numpy as nump
from DSA import BinarySearch


# The Function BinarySearch is imported from another module.

def RemoveDuplicates(ar):           # For removing Duplicates
    return nump.array(list(set(ar)))


def Union(arr1, arr2):        # Function to do Union

    union = nump.array([])

    if len(arr1) < len(arr2):                       # Check if the size of 2nd array is greater than the first
        arr1, arr2 = arr2, arr1     # If True swap arr1 with arr2

    union = nump.append(union, arr1)

    for i in arr2:
        if BinarySearch.BinarySearch(list(arr1), i, 0, len(arr1) - 1) == -1:    # If the element(from the 2nd array) is not present in the 1st array
            union = nump.append(union, i)

    print(sorted(union.astype(int)))


def Intersection(arr1, arr2):     # Function to do Intersection

    intersection = nump.array([])

    if len(arr1) < len(arr2):                       # Check if the size of 2nd array is greater than the first
        arr1, arr2 = arr2, arr1     # If True swap arr1 with arr2

    for i in arr2:
        if BinarySearch.BinarySearch(list(arr1), i, 0, len(arr1) - 1) != -1:    # If the element(from the 2nd array) is not present in the 1st array
            intersection = nump.append(intersection, i)

    print(sorted(intersection.astype(int)))


if __name__ == '__main__':
    try:
        array1 = nump.array(list(map(int, input("Enter the 1st array: ").strip().split(' '))))
        array2 = nump.array(list(map(int, input("Enter the 2nd array: ").strip().split(' '))))

        print("Union: ", end='')
        Union(array1, array2)

        print("Intersection: ", end='')
        Intersection(array1, array2)

    except Exception as e:
        print("Error: " + str(e))
