
def SquareRoot(a, c):
    if pow(a, 2) < pow(c, 2):
        return True


def CountTriplets(n):


    for num in range(n+1):
        


if __name__ == "__main__":
    try:
        n = int(input("Enter the Value of N: ").strip())
        CountTriplets(n)

    except Exception as e:
        print("Error: " + str(e))
