def solution(arr):
    answer = []
    
    # 첫 번째 원소는 무조건 추가
    answer.append(arr[0])
    
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            answer.append(arr[i])
            
    return answer

# 테스트 케이스
if __name__ == "__main__":
    arr_list = [[1, 1, 3, 3, 0, 1, 1], [4, 4, 4, 3, 3]]
    for arr in arr_list:
        result = solution(arr)
        print(result)