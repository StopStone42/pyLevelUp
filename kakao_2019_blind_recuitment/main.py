def solution(N, stages):
    answer = {}

    users = len(stages)
    for i in range(1, N+1):
        if users == 0:
            answer[i] = 0
            continue
        cnt = stages.count(i)
        answer[i] = cnt / users
        users -= cnt
    print(answer)
    return sorted(answer, key=lambda x : answer[x], reverse=True)


if __name__ == '__main__':
    print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
