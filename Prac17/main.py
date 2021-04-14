from math import factorial

def solution(n, k):
    answer = []
    nl = list(range(1, n+1))

    while n != 0:
        fact = factorial(n-1)
        answer.append(nl.pop((k-1)//fact))
        n-=1
        k%=fact
    return answer

if __name__ == '__main__':
    print(solution(3, 5))