def solution(n, times):
    left, right = 1, max(times) * n # 최소 1분 ~ 최대 n명이 가장 느린 심사관에게 모두 가는 경우
    answer = right  # 최솟값을 찾는 문제이므로 초기값을 최대 값으로 설정
    
    while left <= right:
        mid = (left + right) // 2
        total = sum(mid // time for time in times)  # mid 분 동안 처리 가능한 총 인원
        
        if total >= n:  # 모든 사람을 처리할 수 있다면, 시간을 줄여보기
            answer = mid
            right = mid - 1
        else:   # 처리할 수 없다면, 시간을 늘리기
            left = mid + 1
            
    return answer

# 테스트 케이스
if __name__ == "__main__":
    n_list = [6, 10]
    times_list = [[7, 10], [1, 2, 3]]
    for n, times in zip(n_list, times_list):
        result = solution(n, times)
        print(result)