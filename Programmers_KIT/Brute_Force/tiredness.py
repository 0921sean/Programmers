from itertools import permutations

def solution(k, dungeons):
    max_dungeons = 0
    
    for perm in permutations(dungeons):
        fatigue = k # 피로도
        count = 0
        
        for min_required, consumed in perm:
            if fatigue >= min_required:
                fatigue -= consumed
                count += 1
            else:
                break
        max_dungeons = max(max_dungeons, count)
        
        if max_dungeons == len(dungeons):
            break
            
    return max_dungeons
            
# 테스트 케이스
if __name__ == "__main__":
    k_list = [80]
    dungeons_list = [[[80, 20], [50, 40], [30, 10]]]
    for k, dungeons in zip(k_list, dungeons_list):
        result = solution(k, dungeons)
        print(result)