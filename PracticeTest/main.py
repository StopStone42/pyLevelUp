def solution(answers):
    answer = []
    score = [0, 0, 0]

    stu_1 = [1, 2, 3, 4, 5]
    stu_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    stu_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i, answers in enumerate(answers):
        if answers == stu_1[i % len(stu_1)]:
            score[0] += 1
        if answers == stu_2[i % len(stu_2)]:
            score[1] += 1
        if answers == stu_3[i % len(stu_3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            answer.append(idx + 1)
    return answer


if __name__ == '__main__':
    print(solution([1, 2, 3, 4, 5]))
