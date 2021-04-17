"""------------------
Binary Search Program
------------------"""
from time import sleep


# Function for Binary Search
def BinarySearch(ar, searchObj, start, end):
    while start < end:
        middle = (start + end) // 2
        if searchObj == ar[middle]:
            return middle
        elif searchObj < ar[middle]:
            end = middle                # if the element is at tha left side from middle
        elif searchObj > ar[middle]:
            start = middle              # if the element is at tha right side from middle
    return -1


# Loading Screen type dots
def loading():
    for _ in range(3):
        print('.', end='')
        sleep(0.75)


if __name__ == '__main__':
    arr = list(map(int, input("Enter the Array: ").strip().split(' ')))
    try:
        s = int(input("Enter the value to be search: "))

        print("Sorting the array", end='')
        loading()

        index = BinarySearch(arr, s, 0, len(arr) - 1)

        print("\nSearching", end='')
        loading()

        print("\nValue found at index(Sorted Array): " + str(index))

    except ValueError:
        print("Error! Aborting", end='')
        loading()
