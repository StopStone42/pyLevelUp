def solution(name):
    minVal = [min(ord(i) - ord("A"), ord("Z") - ord(i)+1) for i in name]
    idx, answer = 0, 0
    while True:
        answer += minVal[idx]
        minVal[idx] = 0
        if sum(minVal) == 0:
            break
        l, r = 0,0
        while minVal[idx - l] == 0:
            l += 1
        while minVal[idx + r] == 0:
            r += 1
        answer += l if l < r else r
        idx += -l if l < r else r
    return answer

if __name__ == '__main__':
    print(solution("JEROEN"))