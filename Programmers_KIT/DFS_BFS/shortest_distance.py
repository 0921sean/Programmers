from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    moved = [[-1 for _ in range(m)] for _ in range(n)]
    directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    answer = []
    
    queue = deque()
    queue.append((0, 0))
    moved[0][0] = 1
    
    while queue:
        x, y = queue.popleft()
        
        if x == m-1 and y == n-1:
            return moved[y][x]
        
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            
            if 0 <= nx < m and 0 <= ny < n and maps[ny][nx] == 1 and moved[ny][nx] == -1:
                moved[ny][nx] = moved[y][x] + 1
                queue.append((nx, ny))
    
    return -1

# Solution 클래스 인스턴스 생성 및 함수 호출
if __name__ == "__main__":
    maps_list = [[[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]], [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]]
    for maps in maps_list:
        result = solution(maps)
        print(result)