def solution(number, k):
    stack = []
    
    # 숫자를 하나씩 확인
    for digit in number:
        # 스택이 비어있지 않고, k가 0보다 크고, 스택의 마지막 숫자가 현재 숫자보다 작으면 제거
        while stack and k > 0 and stack[-1] < digit:
            stack.pop()
            k -= 1
        
        # 현재 숫자를 스택에 추가
        stack.append(digit)
        
    # 모든 숫자를 확인한 후에도 k가 남아있다면, 뒤에서부터 k개를 제거
    # number는 내림차순으로 정렬되어 있음
    if k > 0:
        stack = stack[:-k]
        
    # 스택에 있는 숫자들을 문자열로 정렬
    return ''.join(stack)

# 테스트 케이스
if __name__ == "__main__":
    number_list = ["1924", "1231234", "4177252841"]
    k_list = [2, 3, 4]
    for number, k in zip(number_list, k_list):
        result = solution(number, k)
        print(result)