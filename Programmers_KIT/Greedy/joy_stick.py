def solution(name):
    # 알파벳 변경에 필요한 조작 횟수 계산
    def get_change_count(char):
        return min(ord(char) - ord('A'), 26 - (ord(char) - ord('A')))
    
    # 알파벳 변경에 필요한 총 조작 횟수
    change_count = sum(get_change_count(char) for char in name)
    
    # 세 가지 경로 중 최솟값 선택:
    # 1. 기본 경로: 처음부터 끝까지 오른쪽으로 이동
    # 2. 왕복 경로1: i 위치까지 오른쪽으로 갔다가 다시 돌아와서 왼쪽으로 이동
    # 3. 왕복 경로2: 처음부터 왼쪽으로 이동 후 i 위치까지 오른쪽으로 이동
    
    # 첫 번째 경로
    length = len(name)
    min_move = length - 1
    
    for i in range(length):
        next_i = i + 1
        while next_i < length and name[next_i] == 'A':
            next_i += 1
            
        # 왕복 경로1: 0 -> i -> 0 -> (length-1)-(next_i-1)
        route1 = i * 2 + (length - next_i)
        
        # 왕복 경로2: 0 -> (length-1)-(next_i-1) -> i
        route2 = (length - next_i) * 2 + i
        
        min_move = min(min_move, route1, route2)
        
    return change_count + min_move

# 테스트 케이스
if __name__ == "__main__":
    name_list = ["JEROEN", "JAN", "JAAAANK", "BBABAAAB", "BBBABAAAAAAB"]
    for name in name_list:
        print(solution(name))