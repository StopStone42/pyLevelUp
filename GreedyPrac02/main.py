def solution(people, limit):
    people.sort()

    boat = 0
    a = 0
    b = len(people) - 1

    while a < b:
        if people[b] + people[a] <= limit:
            a += 1
            boat += 1
        b -= 1
    return len(people) - boat


if __name__ == '__main__':
    print(solution([70, 80, 50,50], 100))