from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    # 좌표 2배 확장 (다각형 사이 경로 구분을 위해)
    field = [[-1] * 102 for _ in range(102)]
    
    # 다각형 영역 표시
    for rect in rectangle:
        x1, y1, x2, y2 = map(lambda x: x*2, rect)
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                # 다각형 내부 표시
                if x1 < i < x2 and y1 < j < y2:
                    field[i][j] = 0
                # 내부 제외하고 테두리 표시
                elif field[i][j] != 0:
                    field[i][j] = 1
    
    # 시작점, 목표점 모두 2배 확장
    characterX *= 2
    characterY *= 2
    itemX *= 2
    itemY *= 2
    
    # BFS
    queue = deque([(characterX, characterY, 0)])
    field[characterX][characterY] = -1  # 방문 표시
    
    while queue:
        x, y, distance = queue.popleft()  # 위치, 이동거리
        
        # 아이템 위치 도달한 경우
        if x == itemX and y == itemY:
            return distance // 2    # 원래 거리로 변환
        
        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx <= 101 and 0 <= ny <= 101 and field[nx][ny] == 1:
                field[nx][ny] = -1  # 방문 기록
                queue.append((nx, ny, distance + 1))
    
    # 아이템 위치에 도달할 수 없는 경우
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