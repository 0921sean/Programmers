def solution(s):
    # 스택을 이용한 풀이
    stack = []
    
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if not stack:
                return False
            stack.pop()
    
    return len(stack) == 0
    
    # 아래 풀이도 가능
    # count = 0
    
    # for par in s:
    #     if par == "(":
    #         count += 1
    #     else:
    #         if count == 0:
    #             return False
    #         count -= 1
    # if count == 0:
    #     return True
    # else:
    #     return False
    
# 테스트 케이스
if __name__ == "__main__":
    s_list = ["()()", "(())()", ")()(", "(()("]
    for s in s_list:
        result = solution(s)
        print(result)