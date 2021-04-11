def solution(n, money):
    answer = 0
    m = [1] + [0] * n

    for coin in money:
        for price in range(coin, n+1):
            if price >= coin:
                m[price] += m[price - coin]
    return m[n] % 1000000007


if __name__ == '__main__':
    print(solution(5, [1,2,5]))