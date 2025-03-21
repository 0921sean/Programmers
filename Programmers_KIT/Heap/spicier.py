import heapq

def solution(scoville, K):
    heapq.heapify(scoville) # 최소 힙으로 변환
    mix_count = 0   # 섞는 횟수
    
    while len(scoville) > 1:
        min1 = heapq.heappop(scoville)  # 가장 작은 값
        if min1 >= K:
            return mix_count
        
        min2 = heapq.heappop(scoville)  # 두 번째로 작은 값
        new_scoville = min1 + (min2 * 2)
        heapq.heappush(scoville, new_scoville)  # 새로운 값 삽입
        
        mix_count += 1
    
    # 마지막 원소가 K 이상이면 정답, 그렇지 않으면 -1 반환
    return mix_count if scoville[0] >= K else -1

# 테스트 케이스
if __name__ == "__main__":
    scoville_list = [[1, 2, 3, 9, 10, 12], [1, 2], [1, 2, 3, 9, 10, 12]]
    K_list = [7, 3, 1000]
    for scoville, K in zip(scoville_list, K_list):
        result = solution(scoville, K)
        print(result)