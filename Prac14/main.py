def palindrome(s):
    return s == s[::-1]

def solution(s):
    length = len(s)
    maxVal = -1

    for i in range(length):
        for j in range(i, length+1):
            if palindrome(s[i:j]):
                if maxVal < len(s[i:j]):
                    maxVal = len(s[i:j])
    return maxVal


if __name__ == '__main__':
    print(solution("abcdcba"))