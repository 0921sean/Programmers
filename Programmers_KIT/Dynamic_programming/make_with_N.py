def solution(N, number):
    if N == number:
        return 1
    
    dp = [set() for _ in range(9)]
    
    # N을 i번 이어붙인 숫자 (예: N=5일 때, 5, 55, 555, ...)
    for i in range(1, 9):
        dp[i].add(int(str(N) * i))
        
    # N을 1번부터 8번까지 사용하는 경우 계산
    for i in range(2, 9):
        # j와 i-j개로 만든 숫자들 사이의 사칙연산
        # 예: N을 3번 사용하는 경우 = (N을 1번 사용한 결과와 N을 2번 사용한 결과의 조합) + ...
        for j in range(1, i):
            for op1 in dp[j]:
                for op2 in dp[i-j]:
                    dp[i].add(op1 + op2)
                    dp[i].add(op1 - op2)
                    dp[i].add(op1 * op2)
                    if op2 != 0:
                        dp[i].add(op1 // op2)
                        
        # i번 사용해서 number를 만들 수 있는지 확인
        if number in dp[i]:
            return i
        
    # 8번 이하로 만들 수 없는 경우
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