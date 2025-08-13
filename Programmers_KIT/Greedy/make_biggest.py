def solution(number, k):
    stack = []
    biggest_number = ""
    stop_idx = 0
    
    for num in number:
        if k == 0:
            break
        while k != 0 and stack != [] and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)
        stop_idx += 1
    
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack) + number[stop_idx:len(number)]

# 테스트 케이스
if __name__ == "__main__":
    number_list = ["1924", "1231234", "4177252841", "777777"]
    k_list = [2, 3, 4, 2]
    for number, k in zip(number_list, k_list):
        result = solution(number, k)
        print(result)