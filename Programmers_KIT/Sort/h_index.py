def solution(citations):
    citations.sort(reverse=True)
    for h in range(len(citations), -1, -1):
        # h를 대입해가며, 그 위치의 두 값을 비교 (h가 len(citations)일 때는 하나의 값만을 비교)
        if h == len(citations):
            if citations[h-1] >= h:
                return h
        if citations[h-1] >= h and citations[h] <= h:
            return h

# 테스트할 케이스들
if __name__ == "__main__":
    citations_list = [[3, 0, 6, 1, 5], [12, 11, 10, 9, 8, 1], [6, 6, 6, 6, 6, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]
    for citations in citations_list:
        result = solution(citations)
        print(result)