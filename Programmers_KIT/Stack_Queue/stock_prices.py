from collections import deque

def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = deque() # 가격이 떨어지지 않은 인덱스 저장
    
    for i in range(n):
        # 현재 가격이 이전 가격보다 작은 경우 = 가격이 떨어진 경우
        while stack and prices[i] < prices[stack[-1]]:
            prev_index = stack.pop()
            answer[prev_index] = i - prev_index # 유지 시간 저장
        
        stack.append(i) # 현재 인덱스 추가
        
    # 스택에 남아 있는 인덱스
    while stack:
        prev_index = stack.pop()
        answer[prev_index] = (n - 1) - prev_index   # 유지 시간 저장
    
    return answer

# 테스트 케이스
if __name__ == "__main__":
    prices_list = [[1, 2, 3, 2, 3], [1, 2, 3, 2, 3, 1]]
    for prices in prices_list:
        result = solution(prices)
        print(result)