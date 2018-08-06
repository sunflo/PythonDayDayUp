def fib(maxx):
    a, b = 0, 1
    n = 0
    while n < maxx:
        # print(b)
        yield b
        a, b = b, a + b
        n = n + 1


for f in fib(8):
    print(f)
