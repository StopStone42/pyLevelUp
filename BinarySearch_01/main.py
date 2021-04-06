def solution(n, times):
    answer = 0
    r = min(times) * n
    l = 1

    while l <= r:
        mid = (r + l) // 2
        temp = n
        for i in times:
            temp -= mid // i
            if temp <= 0:
                answer = mid
                r = mid - 1
                break
        if temp > 0:
            l = mid + 1
    return answer

if __name__ == '__main__':
    print(solution(6, [7,10]))