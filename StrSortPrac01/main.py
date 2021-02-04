def solution(strings, n):
    return sorted(sorted(strings), key=lambda strings : strings[n])


if __name__ == '__main__':
    print(solution(["ab","ba","cq","ac"], 1))