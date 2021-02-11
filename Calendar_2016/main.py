def solution(a, b):
    week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    n = [31,29,31,30,31,30,31,31,30,31,30,31]
    tot= b + 4
    for i in range(a-1):
        tot += n[i]

    return week[tot%7]

if __name__ == '__main__':
    print(solution(2, 1))