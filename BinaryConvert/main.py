def solution(s):
    cnt = 0
    zero = 0
    while s != '1':
        zero += s.count('0')
        s = s.replace('0', '')
        s = bin(len(s))[2:]

        cnt += 1
        print(s, cnt)

    return [cnt, zero]


if __name__ == '__main__':
    print(solution("110010101001"))