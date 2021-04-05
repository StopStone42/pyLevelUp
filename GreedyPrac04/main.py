def solution(routes):
    answer = 0

    routes.sort(key=lambda x: x[1])
    camera = -300001

    for route in routes:
        if camera < route[0]:
            answer += 1
            camera = route[1]
    return answer

if __name__ == '__main__':
    print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))