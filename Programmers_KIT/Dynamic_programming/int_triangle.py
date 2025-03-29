def solution(triangle):
    dp = [[0 for _ in range(len(triangle))] for _ in range(len(triangle))]
    
    for i in range(len(triangle)):
        line = triangle[i]
        if len(line) > 1:
            # dp[len(line)-1] = dp[len(line)-1] + line[-1]
            for j in range(1, len(line)):
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + line[j]
        dp[i][0] = dp[i-1][0] + line[0]
        print(dp)
    return max(dp[len(triangle)-1])

# 테스트 케이스
if __name__ == "__main__":
    triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
    
    result = solution(triangle)
    print(result)