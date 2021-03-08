def solution(land):
    answer = 0
    idx = -1
    for i in range(1, len(land)):
        for j in range(len(land[i])):
            land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])

    return max(land[-1])

if __name__ == '__main__':
    print(solution([[1,2,3,5],
                    [5,6,7,8],
                    [4,3,2,1]]))