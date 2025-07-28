def solution(answers):
    number_dict = {
        1: [1, 2, 3, 4, 5],
        2: [2, 1, 2, 3, 2, 4, 2, 5],
        3: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    }
    score_dict = {1: 0, 2: 0, 3: 0}
    high_scores = []
    
    for person, number in number_dict.items():
        for i, answer in enumerate(answers):
            if answer == number[i % len(number)]:
                score_dict[person] += 1
                
    for person, score in score_dict.items():
        if score == max(score_dict.values()):
            high_scores.append(person)
        
    return high_scores

# 테스트할 케이스들
if __name__ == "__main__":
    answers_list = [[1, 2, 3, 4, 5], [1, 3, 2, 4, 2]]
    for answers in answers_list:
        result = solution(answers)
        print(result)