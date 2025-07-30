def solution(numbers, target):
    def dfs(index, result_list):
        # print(f"Index: {index}, Result List: {result_list}")
        if index == len(numbers):
            return result_list.count(target)
        new_result = []
        number = numbers[index]
        for result in result_list:
            new_result.append(result + number)
            new_result.append(result - number)
        index += 1
        return dfs(index,new_result)
            
    return dfs(0, [0])

# Solution 클래스 인스턴스 생성 및 함수 호출
if __name__ == "__main__":
    numbers_list = [[1, 1, 1, 1, 1], [4, 1, 2, 1]]
    target_list = [3, 4]
    for numbers, target in zip(numbers_list, target_list):
        result = solution(numbers, target)
        print(result)