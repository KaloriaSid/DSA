def WaterHeight(arr, n):
    ans = 0
    for i in range(1, n - 1):
        left_max = int(max(arr[0:i+1]))
        right_max = int(max(arr[i:n]))
        ans += min(left_max, right_max) - arr[i]

    return ans


walls_height = list(map(int, input().strip().split(' ')))

total_height = WaterHeight(walls_height, len(walls_height))
print(total_height)
