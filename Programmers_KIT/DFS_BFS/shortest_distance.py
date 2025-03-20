from collections import deque

def solution(maps):
    n = len(maps)       # 행의 개수
    m = len(maps[0])    # 열의 개수
    visited = [[-1 for _ in range(m)] for _ in range(n)]    # 방문 횟수(-1 or NOT) 및 이동 거리
    
    directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
    
    # BFS
    queue = deque()
    queue.append((0, 0))    # (0, 0)에서 출발
    visited[0][0] = 1
    
    while queue:
        x, y = queue.popleft()
        
        # 도착 지점 도달하면 이동 거리 반환
        if x == n-1 and y == m-1:
            return visited[x][y]
        
        # 상하좌우 네 방향에 대해
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            
            # 맵 범위 내이며, 벽이 아니며, 아직 방문하지 않은 경우
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1 # 이전 위치의 거리 + 1
                queue.append((nx, ny))
        
    # 도착 지점에 도달할 수 없는 경우 -1 반환
    return -1

# Solution 클래스 인스턴스 생성 및 함수 호출
if __name__ == "__main__":
    maps_list = [[[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]], [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]]
    for maps in maps_list:
        result = solution(maps)
        print(result)