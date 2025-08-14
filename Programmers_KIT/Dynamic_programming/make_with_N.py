def solution(N, number):
    dp = [set() for _ in range(9)]
    
    for i in range(1, 6):
        dp[i].add(int(str(N) * (i)))
        
    for i in range(2, 9):
        for j in range(1, i):
            for num1 in dp[j]:
                for num2 in dp[i-j]:
                    dp[i].add(num1 + num2)
                    dp[i].add(num1 - num2)
                    dp[i].add(num1 * num2)
                    if num2 != 0:
                        dp[i].add(num1 // num2)
                        
    for i in range(1, 9):
        if number in dp[i]:
            return i
    
    return -1

# 테스트 케이스
if __name__ == "__main__":
    test_cases = [
        (5, 12),  # N=5, number=12
        (2, 11),  # N=2, number=11
    ]
    
    for N, number in test_cases:
        result = solution(N, number)
        print(f"N={N}, number={number} => {result}")