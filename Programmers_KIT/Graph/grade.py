def solution(n, results):
    win_graph = [[False] * (n + 1) for _ in range(n + 1)]
    
    # 주어진 승패 결과 반영
    for winner, loser in results:
        win_graph[winner][loser] = True
        
    # A가 B를 이기고, B가 C를 이기면 A가 C를 이긴다고 표시
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if win_graph[i][k] and win_graph[k][j]:
                    win_graph[i][j] = True
                    
    answer = 0
    for i in range(1, n + 1):
        known_count = 0
        for j in range(1, n + 1):
            if i != j and (win_graph[i][j] or win_graph[j][i]):
                known_count += 1
                
        # 해당 선수와 모든 선수와의 승패가 결정되어 있는 개수 카운트
        if known_count == n-1:
            answer += 1
            
    return answer

# 테스트 케이스
if __name__ == "__main__":
    n = 5
    results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
    
    result = solution(n, results)
    print(result)  # 결과: 2