# -> O(n), O(1)
def reverse(A, start, end):
    while start < end:
        temp = A[start]
        A[start] = A[end]
        A[end] = temp
        start += 1
        end -= 1
def rotate(ar, d, n):
    if d == 0:
        return ar
    reverse(ar, 0, d-1)
    reverse(ar, d, n-1)
    reverse(ar, 0, n-1)


# -> O(n), O(d)
def rotate_1(ar, d, n):
    temp, j = ar[:d], 0
    for i in range(n-d):
        ar[i] = ar[i+d]
    for i in range(n-d, n):
        ar[i] = temp[j]
        j += 1
    return ar


# -> O(n*d), O(1)
def rotate_2(ar, d, n):
    while d > 0:
        temp = ar[0]
        for i in range(n-1):
            ar[i] = ar[i+1]
        ar[n-1] = temp
        d -= 1
    return ar


# -> O(n), O(1)
def cyclicRotation(ar, n):
    i, j = 0, n - 1
    while i != j:
        ar[i], ar[j] = ar[j], ar[i]
        i += 1


# -> O(n), O(1)
def maximumSum(ar, n):
    arrSum, currSum = 0, 0
    for i in range(n):
        arrSum += ar[i]
        currSum += i*ar[i]

    maxSum = currSum
    for i in range(1, n):
        currSum = arrSum + currSum - n*ar[n-i]
        if currSum > maxSum:
            maxSum = currSum

    return maxSum


arr = [1, 2, 3, 4, 5, 6, 7]

print(arr)
