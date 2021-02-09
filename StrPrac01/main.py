def solution(s):
    answer = ''

    s = s.split(" ")

    for i in range(len(s)):
        if i != 0:
            answer+=" "
        for j in range(len(s[i])):
            if j % 2 == 0:
                answer += s[i][j].replace(s[i][j], s[i][j].upper())
            else:
                answer += s[i][j].replace(s[i][j], s[i][j].lower())
    return answer

if __name__ == '__main__':
    print(solution("try hello world"))