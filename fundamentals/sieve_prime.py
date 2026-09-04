def is_sieve(n: int):
    sieve_list = [True] * (n + 1)
    sieve_list[0] = False
    sieve_list[1] = False

    p = 2

    while p * p <= n:

        if sieve_list[p]:
            for multiple in range(p * p, n + 1, p):
                sieve_list[multiple] = False

        p += 1

    return sieve_list


def sieve_prime(n: int):
    sieve_list = is_sieve(n)
    for i in range(2, n + 1):
        if sieve_list[i]:
            print(i, end=" ")


if __name__ == "__main__":
    print(sieve_prime(30))
