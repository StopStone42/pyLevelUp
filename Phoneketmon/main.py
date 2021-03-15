def solution(nums):
    answer = 0
    N = len(nums) // 2
    nums = list(set(nums))

    for val in nums:
        if answer < N:
            answer += 1
    return answer

if __name__ == '__main__':
    print(solution([3,1,2,3]))