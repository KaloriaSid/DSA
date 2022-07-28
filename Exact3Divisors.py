import math


def exactly3Divisors(N):
    number = N
    count_exact_3_factors = 0
    prime = True

    if number <= 3:
        count_exact_3_factors = 0

    sqroot = int(number ** 0.5)

    if sqroot >= 2:
        count_exact_3_factors = 1

    for index in range(2, sqroot + 1):
        prime = True
        if index == 2:
            prime = True
            continue
        elif index == 3:
            count_exact_3_factors += 1
            prime = True
            continue
        elif index == 5:
            count_exact_3_factors += 1
            prime = True
            continue

        if index % 2 == 0 or index % 3 == 0:
            prime = False
            continue

        breakPoint = math.ceil(index ** 0.5) + 1

        if breakPoint <= 5:
            prime = True
            count_exact_3_factors += 1
            continue

        for index2 in range(5, breakPoint + 1, 6):
            if index % index2 == 0 or index % (index2 + 2) == 0:
                prime = False

        if not prime:
            continue

        prime = True
        if prime:
            count_exact_3_factors += 1

    return count_exact_3_factors


n = int(input())
print(exactly3Divisors(n))
