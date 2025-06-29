def solution(nums):
    pocket_dict = {}
    
    # {'포켓몬 번호': '포켓몬 개수'} 형태의 딕셔너리 생성
    for num in nums:
        pocket_dict[num] = pocket_dict.get(num, 0) + 1
    
    # 포켓몬 종류의 개수가 전체 개수의 절반보다 작거나 같으면 그 개수를 반환
    return min(len(pocket_dict), len(nums) // 2)

# Test cases
if __name__ == "__main__":
    nums_list = [[3, 1, 2, 3], [3, 3, 3, 2, 2, 4], [3, 3, 3, 2, 2, 2]]
    for nums in nums_list:
        result = solution(nums)
        print(result)