def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)  # 마지막 도착 지점 추가
    
    left, right = 1, distance   # 최소 거리 범위 설정
    answer = 0
    
    while left <= right:
        mid = (left + right) // 2
        removed = 0 # 제거한 바위 개수
        prev = 0    # 이전 바위 위치
        min_distance = float('inf') # 현재 상황에서의 최소 거리
        
        for rock in rocks:
            if rock - prev < mid:   # 거리가 mid보다 작다면 바위 제거
                removed += 1
                if removed > n:
                    break
            else:   # 거리가 mid 이상이면 유지
                min_distance = min(min_distance, rock - prev)
                prev = rock # 이전 바위 위치 업데이트
                
        if removed > n:
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