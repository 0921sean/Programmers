def solution(brown, yellow):
    total = brown + yellow
    
    for i in range(1, total):
        if total % i == 0:
            if (i - 2) * ((total//i) - 2) == yellow:
                return [(total//i), i]
            
# 테스트 케이스
brown_list = [10, 8, 24]
yellow_list = [2, 1, 24]
for brown, yellow in zip(brown_list, yellow_list):
    result = solution(brown, yellow)
    print(result)