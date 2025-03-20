def solution(clothes):
    hash_map = {}
    answer = 1
    
    for cloth in clothes:
        hash_map[cloth[1]] = hash_map.get(cloth[1], 0) + 1
    
    for count in hash_map.values():
        answer *= (count + 1)
    answer -= 1
        
    return answer

# 테스트할 케이스들
if __name__ == "__main__":
    clothes_list = [[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]], [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]]
    for clothes in clothes_list:
        result = solution(clothes)
        print(result)