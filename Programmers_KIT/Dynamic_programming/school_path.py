def solution(m, n, puddles):
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    dp[1][1] = 1
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue
            if [j, i] in puddles:
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000007
            # print(dp)
    return dp[-1][-1]

# 테스트 케이스
if __name__ == "__main__":
    m = 4
    n = 3
    puddles = [[2, 2]]
    
    result = solution(m, n, puddles)
    print(result)