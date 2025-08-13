def solution(name):
    # 다음, 이전 알파벳 조작 횟수 계산
    change_count = sum(min(ord(char) - ord('A'), 26 - (ord(char) - ord('A'))) for char in name)
    
    # 3가지 경로 중 최솟값 선택:
    # 1. 처음부터 끝까지 오른쪽으로 이동
    # 2. i 위치까지 오른쪽으로 갔다가 다시 돌아와서 왼쪽으로 이동
    # 3. 처음부터 왼쪽으로 이동 후 i 위치까지 오른쪽으로 이동
    n = len(name)
    min_route = n - 1
    
    for i in range(n):
        j = i + 1
        while j < n and name[j] == 'A':
            j += 1
        min_route = min(min_route, 2*i + (n - j), i + 2*(n-j))
    
    return change_count + min_route

# 테스트 케이스
if __name__ == "__main__":
    name_list = ["JEROEN", "JAN", "JAAAANK", "BBABAAAB", "BBBABAAAAAAB"]
    for name in name_list:
        print(solution(name))