def solution(num):
    cnt = 0
    while 1:
        if num == 1:
            break

        if num % 2 == 0:
            num /= 2
            cnt += 1
        elif num % 2 != 0:
            num = num * 3 + 1
            cnt += 1
        if cnt == 500:
            return -1

    return cnt


if __name__ == '__main__':
    print(solution(6))