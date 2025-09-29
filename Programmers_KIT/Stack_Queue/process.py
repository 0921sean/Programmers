def solution(priorities, location):
    # queue = [(0, 2), (1, 1), (2, 3), (3, 2)]
    queue = [(i, p) for i, p in enumerate(priorities)]
    order = 0   # 실행 순서
    
    while queue:
        current = queue.pop(0)  # 우선 현재 요소를 queue에서 제거
        if any(current[1] < q[1] for q in queue):   # 만약 큐의 요소들 중 하나라도 현재 요소보다 우선순위가 높다면
            queue.append(current)   # 현재 요소를 queue의 뒤에 다시 추가해줌
        else:   # 만약 현재 요소가 큐의 모든 요소보다 우선순위가 높거나 같다면
            order += 1  # (queue에 추가하지 않고) 실행 순서 증가
            if current[0] == location:  # 현재 요소의 인덱스가 location과 같다면
                return order    # 실행 순서 반환
            
# 테스트 케이스
if __name__ == "__main__":
    priorities_list = [[2, 1, 3, 2], [1, 1, 9, 1, 1, 1]]
    location_list = [2, 0]
    for priorities, location in zip(priorities_list, location_list):
        result = solution(priorities, location)
        print(result)