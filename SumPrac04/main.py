def solution(arr1, arr2):
    tmp = []
    answer = []
    for i in range(len(arr1)) :
        for j in range(len(arr1[i])) :
            arr1[i][j] += arr2[i][j]
    return arr1

if __name__ == '__main__':
    print(solution([[1], [2]], [[3], [4]]))
