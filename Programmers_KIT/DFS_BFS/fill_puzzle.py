from collections import deque

def solution(game_board, table):
    fill_blocks = 0
    
    empty_spaces = find_pieces(game_board, 0)
    blocks = find_pieces(table, 1)
    
    used = [False] * len(blocks)
    
    for space in empty_spaces:
        for i, block in enumerate(blocks):
            if used[i]:
                continue
                
            if len(space) != len(block):
                continue
                
            if can_fit(space, block):
                used[i] = True
                fill_blocks += len(block)
                break
                
    return fill_blocks

def find_pieces(board, target):
    n = len(board)
    visited = [[False for _ in range(n)] for _ in range(n)]
    directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    pieces = []
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == target and not visited[i][j]:
                piece = []
                queue = deque([(i, j)])
                visited[i][j] = True
                
                while queue:
                    x, y = queue.popleft()
                    piece.append((x, y))
                    
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == target \
                        and not visited[nx][ny]:
                            queue.append((nx, ny))
                            visited[nx][ny] = True
                            
                normalized_piece = normalize(piece)
                pieces.append(normalized_piece)
                
    return pieces

# 정규화: 가장 작은 x, y 값이 0이 되도록 이동
def normalize(coords):
    min_x = min(x for x, y in coords)
    min_y = min(y for x, y in coords)
    return sorted([(x - min_x, y - min_y) for x, y in coords])

# 시계 방향으로 90도 회전하고 정규화
def rotate(coords):
    rotated = [(y, -x) for x, y in coords]
    return normalize(rotated)

# 주어진 공간에 블록이 들어갈 수 있는지 확인
def can_fit(space, block):
    curr = block
    
    for _ in range(4):
        if space == curr:
            return True
        curr = rotate(curr)
        
    return False

# 테스트 케이스
if __name__ == "__main__":
    game_boards_list = [[[1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1], [1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 0]], [[0, 0, 0], [1, 1, 0], [1, 1, 1]]]
    tables_list = [[[1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0], [0, 1, 0, 0, 0, 0]], [[1, 1, 1], [1, 0, 0], [0, 0, 0]]]
    for game_board, table in zip(game_boards_list, tables_list):
        result = solution(game_board, table)
        print(result)