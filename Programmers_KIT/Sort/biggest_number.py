def solution(numbers):
    answer = ""
    mul_numbers = []
    for i, number in enumerate(numbers):
        number = str(number)
        mul_numbers.append([number * (6//len(number)), i])
    mul_numbers.sort(reverse=True)
    for _, index in mul_numbers:
        answer += str(numbers[index])
        
    return str(int(answer))

# 테스트할 케이스들
if __name__ == "__main__":
    numbers_list = [[6, 10, 2], [3, 30, 34, 5, 9], [40, 4, 404, 1000, 0], [0, 0, 0, 0]]
    for numbers in numbers_list:
        result = solution(numbers)
        print(result)