from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    edges = set()
    not_edges = set()
    moved = [[0 for _ in range(101)] for _ in range(101)]
    directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    
    # 테두리 집합 구성
    for rect in rectangle:
        startX, startY, endX, endY = map(lambda x: x * 2, rect)
        for i in range(startX, endX + 1):
            edges.add((i, startY))
            edges.add((i, endY))
        for i in range(startY + 1, endY):
            edges.add((startX, i))
            edges.add((endX, i))
        for i in range(startX + 1, endX):
            for j in range(startY + 1, endY):
                not_edges.add((i, j))     
    edges -= not_edges
                
    queue = deque()
    queue.append((characterX * 2, characterY * 2))
    
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            
            if (nx, ny) in edges and moved[nx][ny] == 0:
                moved[nx][ny] = moved[x][y] + 1
                queue.append((nx, ny))
                # print(f"현재 위치: ({nx}, {ny}), 이동 거리: {moved[nx][ny]}")
                
            if nx == itemX * 2 and ny == itemY * 2:
                return moved[nx][ny] // 2

# 테스트할 케이스들
if __name__ == "__main__":
    test_cases = [
        ([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8, 17),
        ([[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]], 9, 7, 6, 1, 11),
        ([[1,1,5,7]], 1, 1, 4, 7, 9),
        ([[2,1,7,5],[6,4,10,10]], 3, 1, 7, 10, 15),
        ([[2,2,5,5],[1,3,6,4],[3,1,4,6]], 1, 4, 6, 3, 10)
    ]
    
    for i, (rectangle, characterX, characterY, itemX, itemY, expected) in enumerate(test_cases):
        result = solution(rectangle, characterX, characterY, itemX, itemY)
        print(result)