t = int(input())
for _ in range(t):
    n = int(input())
    zero, one = 0, 0
    def fibonacci(n):
        global zero, one
        if n == 0:
            zero += 1
            return 0
        elif n == 1:
            one += 1
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)
    fibonacci(n)
    print(n, zero, one)