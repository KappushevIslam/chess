def f(num):
    l = []
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            l += [i, num // i]
    return sorted(l)


def f1(n):
    l = []
    for i in range(1, n):
        if n % i == 0:
            l += [i]
    return l

print(f(1000000000000))
print(f1(1000000000000))
