from itertools import combinations


def Substring(s, n):
    temp = ""
    temp = [s[x:y] for x, y in combinations(range(n + 1), r=2)]

    return temp


string = input("Enter the string: ").strip()

sub_string = Substring(string, len(string))
for s in sub_string:
    print(s)
