from collections import defaultdict
from itertools import  combinations as comb
def solution(infos, queries):
    answer = []
    info_dict = defaultdict(list)

    for info in infos:
        info = info.split()
        info_key = info[:-1]
        info_val = int(info[-1])
        for i in range(5):
            for c in comb(info_key, i):
                tmp_key = ''.join(c)
                info_dict[tmp_key].append(info_val)

    for key in info_dict.keys():
        info_dict[key].sort()

    for query in queries:
        query = query.split(' ')
        query_score = int(query[-1])
        query = query[:-1]

        for i in range(3):
            query.remove('and')
        while '-' in query:
            query.remove('-')
        tmp_q = ''.join(query)

        if tmp_q in info_dict:
            scores = info_dict[tmp_q]
            if len(scores) > 0:
                start, end = 0, len(scores)
                while end > start:
                    mid = (start + end) // 2
                    if scores[mid] >= query_score:
                        end = mid
                    else:
                        start = mid + 1
                answer.append(len(scores) - start)
        else:
            answer.append(0)
    return answer


if __name__ == '__main__':
    print(solution(["java backend junior pizza 150",
                    "python frontend senior chicken 210",
                    "python frontend senior chicken 150",
                    "cpp backend senior pizza 260",
                    "java backend junior chicken 80",
                    "python backend senior chicken 50"],

                   ["java and backend and junior and pizza 100",
                    "python and frontend and senior and chicken 200",
                    "cpp and - and senior and pizza 250",
                    "- and backend and senior and - 150",
                    "- and - and - and chicken 100",
                    "- and - and - and - 150"]
                   ))