from itertools import permutations

def solution(numbers):
    number_set = set()
    answer = []
    # 숫자의 순열을 구하고, 중복 없애기
    for i in range(1, len(numbers) + 1):
        perms = permutations(numbers, i)    # perms = [('0', '1'), ('0', '1'), ('1', '0'), ('1', '1'), ('1', '0'), ('1', '1')]
        for p in perms:
            number = int(''.join(p))
            number_set.add(number)
    # 소수 판별
    for number in number_set:
        isPrime = True
        if number == 0 or number == 1:
            isPrime = False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                isPrime = False
        if isPrime:
            answer.append(number)
    return len(answer)

# 테스트 케이스
numbers_list = ["17", "011"]
for numbers in numbers_list:
    result = solution(numbers)
    print(result)