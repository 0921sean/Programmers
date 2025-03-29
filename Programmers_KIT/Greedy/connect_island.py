def solution(n, costs):
    # 간선들을 비용에 따라 오름차순으로 정렬
    costs.sort(key=lambda x: x[2])
    
    parent = [i for i in range(n)]
    
    # Find 연산: 노드의 루트 노드를 찾는 함수
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
            
    # Union 연산: 두 집합을 합치는 함수
    def union(a, b):
        a = find(a)
        b = find(b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
            
    total_cost = 0
    edge_count = 0
    
    # 모든 간선을 확인
    for cost in costs:
        a, b, weight = cost
        
        # 사이클을 형성하지 않는 경우에만 집합에 포함
        if find(a) != find(b):
            union(a, b)
            total_cost += weight
            edge_count += 1
            
            # n-1개의 간선이 선택되면 최소 신장 트리 완성
            if edge_count == n - 1:
                break
                
    return total_cost

# 테스트 케이스
if __name__ == "__main__":
    n = 4
    costs = [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]
    print(solution(n, costs))