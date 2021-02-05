import re

def solution(new_id):
    new_id = new_id.lower()  # 1번 대-소문자 변환
    new_id = re.sub(r"[^a-z0-9\-\_\.]", '', new_id)
    new_id = re.sub(r"[\.]+", ".", new_id)

    if new_id.startswith('.'):
        new_id = new_id[1:]
    if new_id.endswith('.'):
        new_id = new_id[:-1]
    if new_id == "":
        new_id += 'a'

    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id.endswith('.'):
            new_id = new_id[:-1]

    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]
    return new_id


if __name__ == '__main__':
    print(solution("...!@BaT#*..y.abcdefghijklm"))
    print(solution("=.="))
