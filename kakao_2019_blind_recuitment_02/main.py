
def solution(record):
    answer = []
    log = []
    logTable = {}

    for i in record:
        tmp = i.split(" ")

        if tmp[0] == 'Enter':
            logTable[tmp[1]] = tmp[2]
            log.append([tmp[1], "님이 들어왔습니다."])
        elif tmp[0] == 'Leave':
            log.append([tmp[1], "님이 나갔습니다."])
        elif tmp[0] == 'Change':
            logTable[tmp[1]] = tmp[2]
    for i in log:
        answer.append(logTable[i[0]] + i[1])

    return answer


if __name__ == '__main__':
    print(solution(["Enter uid1234 Muzi",
                    "Enter uid4567 Prodo",
                    "Leave uid1234",
                    "Enter uid1234 Prodo",
                    "Change uid4567 Ryan"]))