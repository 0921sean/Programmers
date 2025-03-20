def solution(n, computers):
    visited = set() # 방문 기록
    answer = 0
    
    def dfs(node):
        nonlocal answer
        
        visited.add(node)
        
        for neighbor in range(n):
            if computers[node][neighbor] == 1 and neighbor not in visited:
                dfs(neighbor)
                
    for computer in range(n):
        if computer not in visited:
            answer += 1
            dfs(computer)
            
    return answer

# Solution 클래스 인스턴스 생성 및 함수 호출
if __name__ == "__main__":
    n_list = [3, 3]
    computers_list = [[[1,1,0],[1,1,0],[0,0,1]], [[1,1,0],[1,1,1],[0,1,1]]]
    for n, computers in zip(n_list, computers_list):
        result = solution(n, computers)
        print(result)
