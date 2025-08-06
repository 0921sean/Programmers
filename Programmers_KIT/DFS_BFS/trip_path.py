def solution(tickets):
    ways_list = []
      
    def dfs(tickets, way):
        curr = way[-1]
        if not tickets:
            ways_list.append(way)
        for i, (start, end) in enumerate(tickets):
            if start == curr:
                new_way = way[:]
                new_way.append(end)
                dfs(tickets[:i] + tickets[i+1:], new_way)
                
    dfs(tickets, ["ICN"])
    ways_list.sort()
    return ways_list[0]

# 테스트 케이스
test_cases = [
    [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]],
    [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
]

for tickets in test_cases:
    print(solution(tickets))