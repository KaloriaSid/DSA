"""-------------------------------------------------------------------
Program to find two non-repeating elements (i.e. we have 2n+2 numbers
and n numbers are occurring twice and remaining two have occurred once)
-------------------------------------------------------------------"""


from DSA import NumOccurring


def NoOfOccurrence(arr):
    count = NumOccurring.Initialize(arr)        # Initialization

    print("Non-repeating numbers: ", end='')
    for num in arr:
        if count[num] == 1:
            print(num, end=' ')


# Driver Code
if __name__ == "__main__":
    array = list(map(int, input("Enter the list: ").strip().split()))

    NoOfOccurrence(array)
