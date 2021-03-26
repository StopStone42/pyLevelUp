import math

def solution(w,h):
    gcd = math.gcd(w, h)
    return w * h - (w+h-gcd)


if __name__ == '__main__':
    print(solution(8, 12))