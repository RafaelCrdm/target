def perfect_sq(x: int) -> int:
    sqrt = int(x ** 0.5)
    return sqrt * sqrt == x

def fibonacci(n: int) -> int:
    return perfect_sq(5 * n ** 2 + 4) or perfect_sq(5 * n ** 2 - 4)


numero = int(input())
print(fibonacci(numero))
