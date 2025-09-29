def solution(n, costs):
    def ancestor(node, parents):
        if parents[node] == node:
            return node
        else:
            return ancestor(parents[node], parents)
        
    costs.sort(key=lambda x: x[2])  # 비용 기준으로 정렬
    parents = [i for i in range(n)]
    bridges = 0     # 건설된 다리 개수
    total_costs = 0 # 총 다리 건설 비용
    
    for start, end, cost in costs:
        if ancestor(start, parents) != ancestor(end, parents):
            parents[ancestor(start, parents)] = end
            bridges += 1
            total_costs += cost
            # print(f"다리 건설: {start} -> {end}, 비용: {cost}, 총 비용: {total_costs}")
        if bridges == n-1:
            return total_costs
        

# 테스트 케이스
if __name__ == "__main__":
    n = 4
    costs = [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]
    print(solution(n, costs))