"""-------------------------------------------------------------
Python program to print all permutations with duplicates allowed
-------------------------------------------------------------"""


def toString(l):    # Convert list to a string
    return ''.join(l)


def Permutation(string, count, r):
    if count == r:
        print(toString(string))

    for i in range(count, r + 1):
        string[count], string[i] = string[i], string[count]     # Swapping
        Permutation(string, count + 1, r)               # Permutate
        string[count], string[i] = string[i], string[count]     # Swapping


# Driver program
if __name__ == "__main__":

    s = input("Enter your String: ")

    Permutation(list(s), 0, len(s) - 1)
