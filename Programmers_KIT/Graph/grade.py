def solution(n, results):
    # 승패 관계를 저장할 그래프
    # win_graph[a][b] = True이면 a가 b를 이김
    win_graph = [[False] * (n + 1) for _ in range(n + 1)]
    
    # 주어진 경기 결과로 승패 관계 초기화
    for winner, loser in results:
        win_graph[winner][loser] = True
        
    # 간접적인 승패 관계까지 파악
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                # i가 k를 이기고, k가 j를 이기면, i는 j를 이김
                if win_graph[i][k] and win_graph[k][j]:
                    win_graph[i][j] = True
    
    # 각 선수별로 승패 관계가 모두 결정되었는지 확인
    answer = 0
    for i in range(1, n + 1):
        known_count = 0
        for j in range(1, n + 1):
            # i가 j를 이기거나, j가 i를 이기는 경우 승패 관계 알 수 있음
            if i != j and (win_graph[i][j] or win_graph[j][i]):
                known_count += 1
                
        # i 선수가 다른 모든 선수와의 승패 관계를 알 수 있다면
        if known_count == n - 1:
            answer += 1
            
    return answer

# 테스트 케이스
if __name__ == "__main__":
    n = 5
    results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
    
    result = solution(n, results)
    print(result)  # 결과: 2