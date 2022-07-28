def MinMaxComp(arr, n):
    mi, mx = arr[0], arr[0]

    if n == 1:
        return mi, mx

    if arr[0] > arr[1]:
        mi = arr[1]
        mx = arr[0]
    else:
        mi = arr[0]
        mx = arr[1]

    for i in range(2, n):
        if arr[i] > mx:
            mx = arr[i]
        elif arr[i] < mi:
            mi = arr[i]

    return mi, mx


A = [1000, 11, 445, 1, 330, 3000]
minA, maxA = MinMaxComp(A, len(A))
print(minA, ' ', maxA)
