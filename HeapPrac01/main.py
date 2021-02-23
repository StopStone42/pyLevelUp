import heapq

def solution(scoville, K):
    heap = []
    mix = 0

    for i in scoville:
        heapq.heappush(heap, i)

    while heap[0] < K:
        try:
            heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))
        except IndexError:
            return -1
        mix += 1
    return mix


if __name__ == '__main__':
    print(solution([1, 2, 3, 9, 10, 12], 7))