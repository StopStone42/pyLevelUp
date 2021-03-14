def solution(files):
    answer = []
    idx = 0
    for f in files:
        f = f.lower()
        H = ""
        for i in range(len(f)):
            if f[i].isdigit():
                f = f[i:]
                break
            else:
                H += f[i]

        N = ""
        for i in range(len(f)):
            if f[i].isdigit() == False:
                f = f[i:]
                break
            else:
                N += f[i]
        T = f
        answer.append([idx, H, N, T])
        idx += 1

    answer.sort(key=lambda x: (x[1], int(x[2]), x[0]))

    ans = []
    for tup in answer:
        ans.append(files[tup[0]])

    return ans


if __name__ == '__main__':
    print(solution("foo9.txt"))