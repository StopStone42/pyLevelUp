def solution(brown, yellow):
    s = brown + yellow

    for i in range(s, 2, -1):
        if s % i == 0:
            a = s//i
            if yellow == (i-2) * (a-2):
                return [i,a]

if __name__ == '__main__':
    print(solution(10, 2))