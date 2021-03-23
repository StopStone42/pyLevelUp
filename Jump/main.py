def solution(n):
    ans = 0

    while n != 0:
        n, b = divmod(n, 2)
        ans += b
    return ans


if __name__ == '__main__':
    print(solution(5))