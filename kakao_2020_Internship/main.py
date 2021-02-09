def solution(numbers, hand):
    answer = ''
    posL = '*'
    posR = '#'
    pos = \
        {
          1: (0, 0), 2: (0, 1), 3: (0, 2),
          4: (1, 0), 5: (1, 1), 6: (1, 2),
          7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2),
    }

    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            answer += 'L'
            posL = i
        elif i == 3 or i == 6 or i == 9:
            answer += 'R'
            posR = i

        else:
            ld = abs(pos[posL][0] - pos[i][0]) + abs(pos[posL][1] - pos[i][1])
            rd = abs(pos[posR][0] - pos[i][0]) + abs(pos[posR][1] - pos[i][1])

            if ld > rd:
                answer += 'R'
                posR = i
            elif ld < rd:
                answer += 'L'
                posL = i
            else:
                if hand == "right":
                    answer += 'R'
                    posR = i
                else:
                    answer += 'L'
                    posL = i
    return answer


if __name__ == '__main__':
    print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
