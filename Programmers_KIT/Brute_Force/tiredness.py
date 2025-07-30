from itertools import permutations

def solution(k, dungeons):
    max_num = 0 # 최대 던전 개수
    for perm in permutations(dungeons, len(dungeons)):
        fatigue = k # 현재 피로도
        num = 0 # 현재 던전 개수
        for dungeon in perm:
            min_need, cost = dungeon[0], dungeon[1]
            if fatigue >= min_need:
                fatigue -= cost
                num += 1
        if num > max_num:
            max_num = num
        # print(f"Current permutation: {perm}, Fatigue left: {fatigue}, Dungeons cleared: {num}")
    return max_num
            
# 테스트 케이스
if __name__ == "__main__":
    k_list = [80]
    dungeons_list = [[[80, 20], [50, 40], [30, 10]]]
    for k, dungeons in zip(k_list, dungeons_list):
        result = solution(k, dungeons)
        print(result)