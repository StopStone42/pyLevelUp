import math


def solution(n):
    sqN = math.sqrt(n)

    if sqN % 1 == 0.0:
        sqN = math.pow(sqN + 1, 2)
    else:
        sqN = -1

    return int(sqN)

if __name__ == '__main__':
    print(solution(121))