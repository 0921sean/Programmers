def solution(array, commands):
    answer = []    
    for command in commands:
        i, j, k = command
        sorted_array = sorted(array[i-1:j])
        answer.append(sorted_array[k-1])
    return answer

# 테스트할 케이스들
if __name__ == "__main__":
    array_list = [[1, 5, 2, 6, 3, 7, 4]]
    commands_list = [[[2, 5, 3], [4, 4, 1], [1, 7, 3]]]
    for array, command in zip(array_list, commands_list):
        result = solution(array, command)
        print(result)