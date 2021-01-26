def solution(phone_number):
    answer = ''

    for i in range(len(phone_number) - 4):
        answer += '*'
    answer += phone_number[-4:]
    return answer


if __name__ == '__main__':
    print(solution("01033334444"))
