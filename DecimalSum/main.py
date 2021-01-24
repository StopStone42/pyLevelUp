def solution(a, b):
    answer = 0

    if a >= b:
        answer = sum(range(b, a + 1))
    elif a < b:
        answer = sum(range(a, b + 1))
    return answer


if __name__ == '__main__':
    print(solution(5,3))