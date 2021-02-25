def solution(n, words):
    answer = [0, 0]
    cnt = 1

    for idx in range(1, len(words)):
        word = words[idx]
        cnt %= n
        if (word in words[0:idx]) or (words[idx-1][-1] != word[0]):
            answer = [cnt +1, 1 + idx//n]
            return answer
        cnt += 1
    return answer


if __name__ == '__main__':
    print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))