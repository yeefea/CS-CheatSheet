def fibonacci(n):
    if n < 2:
        return 1
    last = 1
    next_to_last = 1
    answer = 1
    for i in range(2, n + 1):
        answer = last + next_to_last
        next_to_last = last
        last = answer
    return answer


def fibonacci_slow(n):
    if n < 2:
        return 1
    return fibonacci_slow(n - 1) + fibonacci_slow(n - 2)


for i in range(10):
    print(fibonacci(i))
