import heapq

def solution(n, works):
    answer = 0
    h = []

    for work in works:
        heapq.heappush(h, (-work, work))

    while True:
        if n == 0:
            break
        work = heapq.heappop(h)[1]-1
        heapq.heappush(h, (-work, work))
        n -= 1

    for i in h:
        if i[1] < 0:
            continue
        answer += i[1] ** 2
    return answer


if __name__ == '__main__':
    print(solution(4, [4, 3, 3]))