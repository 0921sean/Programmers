from collections import defaultdict, deque

def solution(n, edge):
    # 그래프 구성 (인접 리스트 방식)
    graph = defaultdict(list)
    for a, b in vertex:
        graph[a].append(b)
        graph[b].append(a)  # 양방향 간선
        
    # BFS를 위한 준비
    distances = [-1] * (n + 1)  # 각 노드까지의 거리 (-1은 미방문)
    distances[1] = 0    # 시작 노드(1번)까지의 거리는 0
    
    queue = deque([1])  # BFS를 위한 큐, 시작은 1번 노드
    
    # BFS 수행
    while queue:
        current = queue.popleft()
        
        # 현재 노드의 인접 노드 탐색
        for neighbor in graph[current]:
            # 아직 방문하지 않은 인접 노드라면
            if distances[neighbor] == -1:
                # 거리 갱신 (현재 노드 거리 + 1)
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)
                
    # 가장 멀리 떨어진 노드의 거리 구하기
    max_distance = max(distances[1:])   # 0번 노드는 제외
    
    count = distances.count(max_distance)
    
    return count

# 테스트 케이스
if __name__ == "__main__":
    n = 6
    vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
    
    result = solution(n, vertex)
    print(result)  # 결과: 3