import timeit
from itertools import combinations_with_replacement


def find_narcissists(k):
    narcissists = set()

    for n in range(1, 10**k):
        if narcissistic_sum(n) == n:
            narcissists.add(n)

    return sorted(narcissists)


def digits_to_int(digits):
    num = 0
    for k, n in enumerate(digits[::-1]):
        num += n * 10**k
    return num


def int_to_digits(num, sorted=False):
    digits = []
    n = num

    while n > 0:
        z = len(digits) + 1
        d = (n % 10 ** z)
        div = 10 ** (z-1)
        digits.append(int(d / div))
        n = n - d
    return tuple(digits[::-1])


def narcissistic_sum(n):
    if isinstance(n, int):
        n = int_to_digits(n)
    sum = 0
    for i in n:
        sum += i**len(n)
    return sum


def find_narcissists_efficiently(k):
    narcissists = set()
    for l in range(1, k + 1):
        from itertools import combinations
        for c in [tuple(sorted(i)) for i in combinations_with_replacement(range(0, 10), l)]:
            sum = narcissistic_sum(c)
            sum_tuple = tuple(sorted(int_to_digits(sum)))
            if sum_tuple == c:
                narcissists.add(sum)
    return sorted(narcissists)


print(timeit.timeit('print(find_narcissists_efficiently(5))', globals=globals(), number=1))
print(timeit.timeit('print(find_narcissists(5))', globals=globals(), number=1))
