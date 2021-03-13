def solution(s):
    answer = []
    s = s.split(' ')

    for i in s:
        if i.isalpha():
            i = i[0].upper() + i[1:].lower()
        answer.append(i)
    return ' '.join(answer)


if __name__ == '__main__':
    print(solution("3people unFollowed me"))