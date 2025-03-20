def solution(numbers):
    numbers = list(map(str, numbers))
    
    # numbers의 최대가 1000이기 때문에 문자열을 3번만 반복함
    numbers.sort(key=lambda x: x*3, reverse=True)
    
    return ''.join(numbers)

# 테스트할 케이스들
if __name__ == "__main__":
    numbers_list = [[6, 10, 2], [3, 30, 34, 5, 9]]
    for numbers in numbers_list:
        result = solution(numbers)
        print(result)