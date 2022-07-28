"""----------------------------------------------------------
Python program to check for the sum condition to be satisfied
----------------------------------------------------------"""


def PairOfNum(arr, totalSum):
    pair = set()
    count = 0

    for num in arr:
        temp = totalSum - num
        if temp in pair:
            print("(" + str(num) + ", " + str(temp) + ")")
            count += 1
        pair.add(num)

    if count == 0:
        print("No valid Pairs Found")


# Driver Code
if __name__ == "__main__":
    try:
        array = list(map(int, input("Enter the Array: ").strip().split(' ')))
        total = int(input("Enter the Sum: "))
        PairOfNum(array, total)

    except Exception as e:
        print("Error: " + str(e))
