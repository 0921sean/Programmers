def solution(arr):
    stack = []
    
    for num in arr:
        if len(stack) == 0 or num != stack[-1]:
            stack.append(num)
            
    return stack

# 테스트 케이스
if __name__ == "__main__":
    arr_list = [[1, 1, 3, 3, 0, 1, 1], [4, 4, 4, 3, 3]]
    for arr in arr_list:
        result = solution(arr)
        print(result)