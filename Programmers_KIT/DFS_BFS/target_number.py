def solution(numbers, target):
    answer = 0
    
    def dfs(index, sum):
        nonlocal answer
        if index == len(numbers):
            if sum == target:
                answer += 1
            return
        
        # 현재 수를 더하는 경우
        dfs(index + 1, sum + numbers[index])
        
        # 현재 수를 빼는 경우
        dfs(index + 1, sum - numbers[index])
        
    # 0번 인덱스, sum=0부터 시작
    dfs(0, 0)
    
    return answer

# Solution 클래스 인스턴스 생성 및 함수 호출
if __name__ == "__main__":
    numbers_list = [[1, 1, 1, 1, 1], [4, 1, 2, 1]]
    target_list = [3, 4]
    for numbers, target in zip(numbers_list, target_list):
        result = solution(numbers, target)
        print(result)