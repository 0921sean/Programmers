def solution(n, wires):
    graph = [[] for _ in range(n+1)]    # 1부터 n까지 노드 번호
    
    # 양방향 연결
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
        
    # 노드 개수 세기
    def count_nodes(node, parent):
        count = 1
        for neighbor in graph[node]:
            if neighbor != parent:
                count += count_nodes(neighbor, node)
        return count
    
    min_diff = n    # 최소 차이값
    
    for v1, v2 in wires:
        # 임시적으로 양방향 연결 해제
        graph[v1].remove(v2)
        graph[v2].remove(v1)
        
        count1 = count_nodes(v1, -1)
        count2 = n - count1
        
        diff = abs(count1 - count2)
        min_diff = min(min_diff, diff)
        
        # 다시 연결
        graph[v1].append(v2)
        graph[v2].append(v1)
        
    return min_diff

# 테스트 케이스
if __name__ == "__main__":
    n_list = [9, 4, 7]
    wires_list = [[[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]], [[1, 2], [2, 3], [3, 4]], [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]]
    for n, wires in zip(n_list, wires_list):
        result = solution(n, wires)
        print(result)