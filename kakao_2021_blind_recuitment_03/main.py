from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    print(sorted(orders))
    for c in course:
        temp = []
        for order in orders:
            comb = combinations(sorted(orders), c)
            temp += comb
        cnt = Counter(temp)
        if len(cnt) != 0 and max(cnt.values()) != 1:
            answer += [''.join(f) for f in cnt if cnt[f] == max(cnt.values())]
    return sorted(answer)

if __name__ == '__main__':
    print(solution(["ABCFG",
                    "AC",
                    "CDE",
                    "ACDE",
                    "BCFG",
                    "ACDEH"], [2,3,4]))