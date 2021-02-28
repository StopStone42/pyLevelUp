def solution(s):
    answer = ''

    s = list(map(int, s.split(' ')))
    answer = str(min(s)) + " " + str(max(s))

    return answer

if __name__ == '__main__':
    print(solution("1 2 3 4"))