def solution(n):
    x = bin(n).count('1')
    for m in range(n+1, 1000001):
        if bin(m).count('1') == x:
            return m

if __name__ == '__main__':
    print(solution(78))