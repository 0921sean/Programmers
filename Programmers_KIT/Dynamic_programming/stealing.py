def solution(money):
    n = len(money)
    
    # 첫 번째 집을 털고 마지막 집을 털지 않는 경우
    dp1 = [0] * n
    dp1[0] = money[0]
    dp1[1] = max(money[0], money[1])
    
    for i in range(2, n-1):
        dp1[i] = max(dp1[i-1], dp1[i-2] + money[i])
    
    # 첫 번째 집을 털지 않고 마지막 집을 털 수 있는 경우
    dp2 = [0] * n
    dp2[0] = 0
    dp2[1] = money[1]
    
    for i in range(2, n):
        dp2[i] = max(dp2[i-1], dp2[i-2] + money[i])
        
    return max(dp1[n-2], dp2[n-1])

# 테스트 케이스
if __name__ == "__main__":
    money = [1, 2, 3, 1]
    
    result = solution(money)
    print(result)  # 결과: 4