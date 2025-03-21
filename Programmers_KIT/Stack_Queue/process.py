def solution(priorities, location):
    queue = [(i, p) for i, p in enumerate(priorities)]
    execution_order = 0
    
    while queue:
        current = queue.pop(0)
        if any(current[1] < q[1] for q in queue):
            queue.append(current)
        else:
            execution_order += 1
            if current[0] == location:
                return execution_order
            
# 테스트 케이스
if __name__ == "__main__":
    priorities_list = [[2, 1, 3, 2], [1, 1, 9, 1, 1, 1]]
    location_list = [2, 0]
    for priorities, location in zip(priorities_list, location_list):
        result = solution(priorities, location)
        print(result)