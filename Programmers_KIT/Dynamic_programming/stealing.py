def solution(money):
    n = len(money)
    dp = [0 for _ in range(n)]
    
    # 첫 번째 집을 털고 마지막 집을 털지 않는 경우
    dp[0] = money[0]
    dp[1] = money[0]
    
    for i in range(2, n-1):
        dp[i] = max(dp[i-1], dp[i-2] + money[i])
    max_money = dp[n-2]
    
    # 첫 번째 집을 털지 않는 경우 (마지막 집을 털 수 있음)
    dp[0] = 0
    dp[1] = money[1]
    
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + money[i])
    max_money = max(max_money, dp[n-1])
    
    return max_money

# 테스트 케이스
if __name__ == "__main__":
    money = [1, 2, 3, 1]
    
    result = solution(money)
    print(result)  # 결과: 4