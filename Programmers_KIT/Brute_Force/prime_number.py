from itertools import permutations

def solution(numbers):
    nums = []
    
    for i in range(1, len(numbers)+1):
        perms = list(permutations(numbers, i))
        for perm in perms:
            nums.append(int(''.join(perm)))
    
    nums = set(nums)
    
    count = 0
    for num in nums:
        if is_prime(num):
            count += 1
            
    return count

def is_prime(num):
    # 0 또는 1인 경우 소수 아님
    if num < 2:
        return False
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
        
    return True

# 테스트 케이스
numbers_list = ["17", "011"]
for numbers in numbers_list:
    result = solution(numbers)
    print(result)