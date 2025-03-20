def solution(answers):
    correct_list = []   # 정답 개수
    answer = []
    
    # 각 수포자 규칙
    rule_list = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    
    for rule in rule_list:
        question_num = 0
        correct = 0
    
        while question_num < len(answers):
            if answers[question_num] == rule[question_num % len(rule)]:
                correct += 1
            question_num += 1
        correct_list.append(correct)
    
    for idx, correct in enumerate(correct_list):
        if correct == max(correct_list):
            answer.append(idx+1)
    return answer

# 테스트할 케이스들
if __name__ == "__main__":
    answers_list = [[1, 2, 3, 4, 5], [1, 3, 2, 4, 2]]
    for answers in answers_list:
        result = solution(answers)
        print(result)