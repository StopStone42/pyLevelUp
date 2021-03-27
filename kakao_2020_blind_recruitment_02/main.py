def isRight(s):
    stack = 0
    for i in s:
        if i == '(':
            stack += 1
        else:
            stack -= 1
        if stack < 0:
            return False
    return True

def reverse(s):
    ans = ''
    for i in s:
        if i == '(':
            ans += ')'
        else:
            ans += '('
    return ans

def solution(p):
    if p =='': return ''

    stack = 0
    for i in range(len(p)):
        if p[i] == '(':
            stack += 1
        else:
            stack -= 1
        if stack == 0:
            u = p[:i+1]
            v = p[i+1:]
            break

    if isRight(u):
        return u+solution(v)
    else:
        return '(' + solution(v) + ')' + reverse(u[1:-1])

if __name__ == '__main__':
    print(solution(")("))