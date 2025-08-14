def solution(triangle):
    n = len(triangle)
    dp = [[] for _ in range(n)]
    
    dp[0] = triangle[0]
    
    for i in range(1, n):
        dp[i].append(dp[i-1][0] + triangle[i][0])
        for j in range(1, i):
            dp[i].append(max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j])
        dp[i].append(dp[i-1][-1] + triangle[i][-1])
        print(f"dp[{i}]: {dp[i]}")
        
    return max(dp[n-1])

# 테스트 케이스
if __name__ == "__main__":
    triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
    
    result = solution(triangle)
    print(result)