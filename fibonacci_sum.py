def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        prev_ = 0
        prev_x = 1
        current = 1
        for i in range(3, n+1):
            current = prev_ + prev_x
            prev_ = prev_x
            prev_x = current
        return current

sum = 0
for i in range(1, 51):
    sum += fib(i)

print(sum)
