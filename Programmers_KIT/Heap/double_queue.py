import heapq

def solution(operations):
    min_heap = []   # 최소 힙
    max_heap = []   # 최대 힙 (음수 값으로 저장하여 최대 힙처럼 사용)
    entry_set = set()   # 실제 존재하는 값 추적 (동기화 용도)
    
    for op in operations:
        cmd, num = op.split()
        num = int(num)
        
        if cmd == "I":
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            entry_set.add(num)  # 값 추가
        elif cmd == "D":
            if not entry_set:   # 큐가 비어있으면 무시
                continue
            
            if num == 1:    # 최댓값 삭제
                while max_heap:
                    max_val = -heapq.heappop(max_heap)
                    if max_val in entry_set:
                        entry_set.remove(max_val)
                        break
            else:   # 최솟값 삭제
                while min_heap:
                    min_val = heapq.heappop(min_heap)
                    if min_val in entry_set:
                        entry_set.remove(min_val)
                        break
                        
    if not entry_set:   # 큐가 비어있으면 [0, 0] 반환
        return [0, 0]
    
    # 동기화: 남아있는 유효한 최댓값, 최솟값 찾기
    while max_heap and -max_heap[0] not in entry_set:
        heapq.heappop(max_heap)
        
    while min_heap and min_heap[0] not in entry_set:
        heapq.heappop(min_heap)
        
    return [-max_heap[0], min_heap[0]] # [최댓값, 최솟값]

# 테스트 케이스
if __name__ == "__main__":
    operations_list = [
        ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"],
        ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
    ]
    for operations in operations_list:
        result = solution(operations)
        print(result)