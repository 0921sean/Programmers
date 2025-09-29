def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    
    left, right = 1, distance
    
    while left <= right:
        mid = (left + right) // 2
        removed = 0 # 제거된 바위 수
        prev = 0    # 이전 바위 위치
        min_distance = float('inf')
        
        for rock in rocks:
            if rock - prev < mid:
                removed += 1
                if removed > n:
                    break
            else:
                min_distance = min(min_distance, rock - prev)   # 최소 거리 업데이트
                prev = rock
            
        if removed > n: # 제거한 바위 수가 n을 넘으면
            right = mid - 1
        else:
            answer = min_distance
            left = mid + 1
            
    return answer

# 테스트 케이스
if __name__ == "__main__":
    distance_list = [25, 16]
    rocks_list = [[2, 14, 11, 21, 17], [4, 8, 11]]
    n_list = [2, 2]
    for distance, rocks, n in zip(distance_list, rocks_list, n_list):
        result = solution(distance, rocks, n)
        print(result)