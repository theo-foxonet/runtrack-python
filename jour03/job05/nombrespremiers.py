def prime():
    for n in range(0, 1001):
        if n > 1:
            for i in range(2, n):
                if (n % i) == 0:
                    break
            else:
                print(n)

prime()