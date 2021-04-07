def solution(begin, target, words):
    answer = [begin]
    ans_cnt = 0

    if target not in words:
        return 0

    while len(words) != 0:
        for i in answer:
            temp = []
            for word in words:
                count = 0
                for j in range(len(i)):
                    if i[j] != word[j]:
                        count += 1
                    if count == 2:
                        break
                if count == 1:
                    temp.append(word)
                    words.remove(word)
        ans_cnt += 1
        if target in temp:
            return ans_cnt
        else:
            answer = temp
    return 0
if __name__ == '__main__':
    print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))