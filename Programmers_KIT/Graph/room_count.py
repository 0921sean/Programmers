def solution(arrows):
    directions = [
        (0, 1), (1, 1), (1, 0), (1, -1),
        (0, -1), (-1, -1), (-1, 0), (-1, 1)
    ]
    
    visited_nodes = set([(0, 0)])
    visited_edges = set()
    
    room_count = 0
    x, y = 0, 0
    
    for arrow in arrows:
        for _ in range(2):
            dx, dy = directions[arrow]
            nx, ny = x + dx, y + dy
            
            if (nx, ny) in visited_nodes and ((x, y), (nx, ny)) not in visited_edges\
            and ((nx, ny), (x, y)) not in visited_edges:
                room_count += 1
                
            visited_nodes.add((nx, ny))
            
            visited_edges.add(((x, y), (nx, ny)))
            visited_edges.add(((nx, ny), (x, y)))
            
            x, y = nx, ny
            
    return room_count

# 테스트 케이스
if __name__ == "__main__":
    arrows = [6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]
    
    result = solution(arrows)
    print(result)  # 출력: 3