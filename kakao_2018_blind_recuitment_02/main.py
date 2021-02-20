def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        bin_str = bin(arr1[i] | arr2[i])[2:]
        answer.append(("0" *(n - len(bin_str)) + bin_str).replace("1", "#")
                                                      .replace("0", " "))
    return answer


if __name__ == '__main__':
    print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))