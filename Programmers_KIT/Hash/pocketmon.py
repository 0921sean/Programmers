def solution(nums):
    pocket_dict = {}
    
    for num in nums:
        pocket_dict[num] = pocket_dict.get(num, 0) + 1
    
    pocket_num = len(pocket_dict)
    if pocket_num >= len(nums) / 2:
        return len(nums) / 2
    return pocket_num

    # 완전 쉬운 풀이
    # return min(len(nums) // 2, len(set(nums)))

# 테스트할 케이스들
if __name__ == "__main__":
    nums_list = [[3, 1, 2, 3], [3, 3, 3, 2, 2, 4], [3, 3, 3, 2, 2, 2]]
    for nums in nums_list:
        result = solution(nums)
        print(result)