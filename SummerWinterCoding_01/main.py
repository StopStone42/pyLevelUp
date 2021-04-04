def solution(dirs):
    comm = {'U':(0,1), 'D':(0,-1), 'L':(-1,0), 'R':(1,0)}
    road = set()
    x, y = (0,0)

    for dir in dirs:
        tmpX, tmpY = x + comm[dir][0], y + comm[dir][1]
        if -5 <= tmpX <= 5 and -5 <= tmpY <= 5:
            road.add((x,y,tmpX,tmpY))
            road.add((tmpX, tmpY,x,y))
            x, y = tmpX, tmpY
    return len(road) // 2


if __name__ == '__main__':
    print(solution("LULLLLLLU"))