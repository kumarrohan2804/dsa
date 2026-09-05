def fibonacci(n: int) -> list[int]:
    fib_list = []
    a, b = 0, 1
    for _ in range(n):
        fib_list.append(a)
        a, b = b, a + b

    return fib_list


def recursive_fib(n: int) -> list[int]:
    if n <= 0:
        return []

    if n == 1:
        return [0]

    result = recursive_fib(n - 1)
    result.append(result[-1] + (result[-2] if len(result) > 1 else 1))

    return result


if __name__ == "__main__":
    print(*fibonacci(8))
    print(*recursive_fib(10))
