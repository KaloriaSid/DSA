"""----------------------------------------------------
Program to check for majority element in a sorted array
----------------------------------------------------"""


def isMajority(ar, size, num):
    count = 0                           # " Another Method "
    for i in range(size):               # last_index = (size//2 + 1) if size % 2 == 0 else (size//2)     -> last index (middle of the array) as num should be greater than size//2
        if ar[i] == num:                # for i in range(last_index):
            count += 1                      # if ar[i] == num and ar[i + size//2] == num:            -> if num is present and more than size//2
    if count > size // 2:                       # return True
        return True                     # return False
    else:
        return False


if __name__ == "__main__":
    try:
        arr = list(map(int, input("Enter the Array: ").strip().split(' ')))
        x = int(input("Enter the search value: "))

        print(isMajority(arr, len(arr), x))

    except ValueError:
        print("Error!!")
