def solution(nums):
    count_dict = {}
    
    for num in nums:
        if num in count_dict.keys():
            count_dict[num] += 1
        else:
            count_dict[num] = 1
        
    if len(count_dict) >= len(nums) // 2:
        return len(nums) // 2
    
    return len(count_dict)

    # 완전 쉬운 풀이
    # return min(len(nums) // 2, len(set(nums)))

# 테스트할 케이스들
if __name__ == "__main__":
    nums_list = [[3, 1, 2, 3], [3, 3, 3, 2, 2, 4], [3, 3, 3, 2, 2, 2]]
    for nums in nums_list:
        result = solution(nums)
        print(result)