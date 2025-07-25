def solution(arr):
    stack = []
    
    for elm in arr:
        # 스택이 비어있는 경우에는 무조건 추가
        if not stack:
            stack.append(elm)
        # 배열의 원소가 스택의 탑과 값이 다른 경우에만 추가
        if stack[-1] != elm:
            stack.append(elm)
            
    return stack

# Test cases
if __name__ == "__main__":
    arr_list = [[1, 1, 3, 3, 0, 1, 1], [4, 4, 4, 3, 3]]
    for arr in arr_list:
        result = solution(arr)
        print(result)