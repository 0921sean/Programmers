def solution(arr):
    # 숫자와 연산자 분리
    numbers = [int(arr[i]) for i in range(0, len(arr), 2)]
    operators = [arr[i] for i in range(1, len(arr), 2)]
    
    # dp[i][j] = i번째부터 j번째까지 숫자의 연산 결과 중 최댓값과 최솟값
    n = len(numbers)
    max_dp = [[-float('inf')] * n for _ in range(n)]
    min_dp = [[float('inf')] * n for _ in range(n)]
    
    # 초기값 설정: 숫자 하나만 있는 경우
    for i in range(n):
        max_dp[i][i] = numbers[i]
        min_dp[i][i] = numbers[i]
        
    # 연산할 숫자 범위의 크기
    for length in range(1, n):
        # 연산 시작 위치
        for i in range(n - length):
            j = i + length
            
            for k in range(i, j):
                # 현재 연산자
                op = operators[k]
                
                # 가능한 모든 조합 계산
                if op == '+':
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] + max_dp[k+1][j])
                    min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] + min_dp[k+1][j])
                else:   # op == '-'
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] - min_dp[k+1][j])
                    min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] - max_dp[k+1][j])
    
    return max_dp[0][n-1]

# 테스트 케이스
if __name__ == "__main__":
    arr_list = [["1", "-", "3", "+", "5", "-", "8"], ["5", "-", "3", "+", "1", "+", "2", "-", "4"]]
    for arr in arr_list:
        result = solution(arr)
        print(result)  # 결과: 4