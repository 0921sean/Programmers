def solution(arr):
    # 숫자와 연산자 분리
    numbers = [int(arr[i]) for i in range(0, len(arr), 2)]
    operators = [arr[i] for i in range(1, len(arr), 2)]
    
    n = len(numbers)
    max_dp = [[-float('inf') for _ in range(n)] for _ in range(n)]  # 최댓값 dp
    min_dp = [[float('inf') for _ in range(n)] for _ in range(n)]   # 최솟값 dp
    
    # i부터 i까지의 합은 그 자체
    for i in range(n):
        max_dp[i][i] = numbers[i]
        min_dp[i][i] = numbers[i]
        
    for length in range(1, n):
        for i in range(n - length):
            j = i + length
            
            for k in range(i, j):
                op = operators[k]   # 현재 연산자
                
                # i부터 j까지의 합을 반복해서 업데이트
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