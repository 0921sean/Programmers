from collections import deque

def solution(game_board, table):
    n = len(game_board)
    answer = 0
    
    # 게임 보드에서 빈 공간 찾기
    empty_spaces = find_pieces(game_board, 0)
    
    # 테이블에서 블록 찾기 (1을 블록으로 간주)
    blocks = find_pieces(table, 1)
    
    # 사용한 블록을 체크하기 위한 리스트
    used = [False] * len(blocks)
    
    for space in empty_spaces:
        for i, block in enumerate(blocks):
            if used[i]: # 이미 사용한 블록은 건너뛰기
                continue
                
            if len(space) != len(block):
                continue
                
            if can_fit(space, block):
                used[i] = True
                answer += len(block)
                break
                
    return answer

def find_pieces(board, target):
    n = len(board)
    visited = [[False] * n for _ in range(n)]
    pieces = []
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == target and not visited[i][j]:
                # BFS로 연결된 조각 찾기
                piece = []
                queue = deque([(i, j)])
                visited[i][j] = True
                
                while queue:
                    x, y = queue.popleft()
                    piece.append((x, y))
                    
                    for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == target \
                        and not visited[nx][ny]:
                            queue.append((nx, ny))
                            visited[nx][ny] = True
                            
                normalized_piece = normalize(piece)
                pieces.append(normalized_piece)
                
    return pieces

# 좌표를 정규화: 가장 작은 x, y 값이 0이 되도록 이동
def normalize(coords):
    min_x = min(x for x, y in coords)
    min_y = min(y for x, y in coords)
    return sorted([(x - min_x, y - min_y) for x, y in coords])

# 좌표를 시계 방향으로 90도 회전하고 정규화
def rotate(coords):
    rotated = [(y, -x) for x, y in coords]
    return normalize(rotated)

# 블록을 회전시켜 공간에 맞는지 확인
def can_fit(space, block):
    current = block
    
    # 0, 90, 180, 270도 회전 확인
    for _ in range(4):
        if space == current:
            return True
        current = rotate(current)
        
    return False

# 테스트할 케이스들
if __name__ == "__main__":
    game_boards_list = [[[1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1], [1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 0]], [[0, 0, 0], [1, 1, 0], [1, 1, 1]]]
    tables_list = [[[1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0], [0, 1, 0, 0, 0, 1]], [[1, 1, 1], [1, 0, 0], [0, 0, 0]]]
    for game_board, table in zip(game_boards_list, tables_list):
        result = solution(game_board, table)
        print(result)