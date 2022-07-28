def SieveOfEratosthenes(lb, ub):
    prime = [True for i in range(lb, ub + 1)]
    n = 2
    while n * n <= ub:
        if prime[n]:
            for i in range(n * n, ub + 1, n):
                prime[i] = False
        n += 1
    return prime


lower_bound = int(input("Enter the lower bound: "))
upper_bound = int(input("Enter the upper bound: "))

prime_num = SieveOfEratosthenes(lower_bound, upper_bound)
if lower_bound < 2: lower_bound = 2
for i in range(lower_bound, upper_bound + 1):
    if prime_num[i]:
        print(i)
