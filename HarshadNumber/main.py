def solution(x):
    answer = True
    sum = 0

    n = list(str(x))

    for i in range(len(n)):
        sum += int(n[i])

    if x % sum == 0:
        answer = True
    else:
        answer = False
    return answer


if __name__ == '__main__':
    n = int(input())

    answer = solution(n)
    print(answer)