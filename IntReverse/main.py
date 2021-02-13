def solution(n):
    answer = []

    list_n = list(str(n))

    for i in range(len(list_n)-1, -1, -1):
        answer.append(int(list_n[i]))
    return answer


if __name__ == '__main__':
    print(solution(12345))