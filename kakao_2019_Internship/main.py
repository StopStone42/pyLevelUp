def solution(s):
    answer = []
    s = s[2:-2].split('},{')

    s.sort(key=len)
    for i in s:
        init = i.split(',')
        for j in init:
            if int(j) not in answer:
                answer.append(int(j))
    return answer


if __name__ == '__main__':
    print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))