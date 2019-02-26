#3n+1 or n/2

n = 100
while n != 1:
    if n % 2 == 0:
        # even
        n = n // 2
    else:
        n = 3 * n + 1

    print(n, end=', ')

