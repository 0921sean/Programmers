from collections import defaultdict, deque

def solution(n, vertex):
    graph = defaultdict(list)
    for a, b in vertex:
        graph[a].append(b)
        graph[b].append(a)
        
    distances = [-1] * (n + 1)  # 1번 노드로부터의 거리
    distances[1] = 0
    
    queue = deque([1])
    
    # BFS 실행
    while queue:
        current = queue.popleft()
        
        for neighbor in graph[current]:
            # 방문하지 않은 노드라면 (해당 방식으로 1로부터의 거리를 기록할 수 있는 이유는 BFS이기 때문)
            if distances[neighbor] == -1:
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)
                
    max_distance = max(distances)
    
    count = distances.count(max_distance)   # 1번 노드에서 가장 멀리 떨어진 노드의 개수
    
    return count

# 테스트 케이스
if __name__ == "__main__":
    n = 6
    vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
    
    result = solution(n, vertex)
    print(result)  # 결과: 3