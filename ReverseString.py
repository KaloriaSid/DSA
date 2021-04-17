"""--------------------------------------------
Python code to reverse a string using recursion
--------------------------------------------"""


def ReverseString(string):
    if len(string) == 1:
        return string
    return ReverseString(string[1:]) + string[0]


if __name__ == "__main__":
    s = input("Enter the String: ").strip()

    print(ReverseString(s))
