def solution(citations):
    answer = 0

    citations.sort()
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i

    return 0
if __name__ == '__main__':
    print(solution([3, 0, 6, 1, 5]))