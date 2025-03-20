def solution(citations):
    citations.sort()
    
    for h in range(len(citations), 0, -1):
        if citations[len(citations) - h] >= h:
            return h
    return 0

# 테스트할 케이스들
if __name__ == "__main__":
    citations_list = [[3, 0, 6, 1, 5], [12, 11, 10, 9, 8, 1], [6, 6, 6, 6, 6, 1]]
    for citations in citations_list:
        result = solution(citations)
        print(result)