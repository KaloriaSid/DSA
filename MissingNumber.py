"""--------------------------------------------------------
Program to find missing numbers in a list (N-1) from 1 to N
--------------------------------------------------------"""


if __name__ == "__main__":
    try:
        array = sorted(list(map(int, input("Enter the list: ").strip().split(' '))))

        l = [i for i in range(1, array[len(array) - 1] + 1)]

        for num in l:
            if num not in array:
                print(num, end=' ')

    except Exception as e:
        print("Error: " + str(e))
