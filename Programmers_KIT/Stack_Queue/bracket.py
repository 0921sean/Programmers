def solution(s):
    stack = []
    
    for p in s:
        if p == '(':
            stack.append(p)
        else:   # if p == ')'
            if len(stack) == 0 or stack[-1] != '(':
                return False
            stack.pop()
            
    if len(stack) != 0:
        return False
    return True
    
# 테스트 케이스
if __name__ == "__main__":
    s_list = ["()()", "(())()", ")()(", "(()("]
    for s in s_list:
        result = solution(s)
        print(result)