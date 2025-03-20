from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    graph = {}  # 특정 위치에서 이동할 수 있는 위치들
    
    border_points = set()   # 다각형 테두리
    
    # 직사각형 모두 포함
    for rect in rectangle:
        x1, y1, x2, y2 = rect
        
        for x in range(x1, x2 + 1):
            border_points.add((x, y1))
            border_points.add((x, y2))
        for y in range(y1, y2 + 1):
            border_points.add((x1, y))
            border_points.add((x2, y))
        
    # 직사각형 내부 점들을 제거
    for rect in rectangle:
        x1, y1, x2, y2 = rect
        
        for x in range(x1 + 1, x2):
            for y in range(y1 + 1, y2):
                if (x, y) in border_points:
                    border_points.remove((x, y))
                    
    # 움직일 수 있는 테두리 기록
    for x, y in border_points:
        graph[(x, y)] = []
        
        for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if (nx, ny) in border_points:
                graph[(x, y)].append((nx, ny))
                
    print(border_points)
    print(graph)
                
    # BFS
    queue = deque([((characterX, characterY), 0)])
    visited = {(characterX, characterY)}
    
    while queue:
        (x, y), distance = queue.popleft()  # 위치, 이동거리
        
        # 아이템 위치 도달하면 이동거리 반환
        if (x, y) == (itemX, itemY):
            return distance
        
        for nx, ny in graph[(x, y)]:
            if (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), distance + 1))
    
    # 아이템 위치에 도달하지 못하면 -1 반환
    return -1

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
        print(f"테스트 케이스 {i+1}: 결과 = {result}, 기대값 = {expected}, {'성공' if result == expected else '실패'}")