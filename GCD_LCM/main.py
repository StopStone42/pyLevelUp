def solution(n, m):
    return [gcd(n, m), n * m // gcd(n, m)]


def gcd(n, m):
    i = min(n, m)
    while True:
        if n % i == 0 and m % i == 0:
            return i
        i -= 1


if __name__ == '__main__':
    print(solution(2, 5))
