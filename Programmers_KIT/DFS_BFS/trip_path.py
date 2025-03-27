def solution(tickets):
    # 출발 공항 -> 도착 공항 그래프 생성
    graph = {}
    for start, end in tickets:
        if start in graph:
            graph[start].append(end)
        else:
            graph[start] = [end]
            
    # 알파벳 순서가 앞서는 경로를 먼저 방문하기 위해
    for airport in graph:
        graph[airport].sort()
        
    path = ["ICN"]
    
    def dfs(current):
        # 모든 항공권을 사용한 경우
        if len(path) == len(tickets) + 1:
            return True
        
        # 현재 공항이 그래프에 없는 경우
        if current not in graph or not graph[current]:
            return False
        
        # 현재 공항에서 갈 수 있는 공항들을 복사 (백트래킹을 위해)
        temp = graph[current][:]
        
        for i, next_airport in enumerate(temp):
            # 다음 공항으로 이동
            graph[current].pop(i)
            path.append(next_airport)
            
            # DFS 재귀 호출
            if dfs(next_airport):
                return True
            
            # 백트래킹: 현재 경로가 유효하지 않으면 이전 상태로 복원
            path.pop()
            graph[current].insert(i, next_airport)
            
        return False
        
    # "ICN"에서 시작하는 DFS 실행
    dfs("ICN")
    
    return path

# 테스트 케이스
test_cases = [
    [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]],
    [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
]

for tickets in test_cases:
    print(solution(tickets))