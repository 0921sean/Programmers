def solution(word):
    vowels = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    
    # 각 자리에서의 가중치 계산
    # 1번째 자리: 1 + 5 + 5^2 + 5^3 + 5^4 = 781
    # 2번째 자리: 1 + 5 + 5^2 + 5^3 = 156
    # 3번째 자리: 1 + 5 + 5^2 = 31
    # 4번째 자리: 1 + 5 = 6
    # 5번째 자리: 1
    weights = [781, 156, 31, 6, 1]
    
    answer = 0
    for i, char in enumerate(word):
        answer += vowels[char] * weights[i] + 1
        
    return answer

# 테스트 케이스
if __name__ == "__main__":
    word_list = ["AAAAE", "AAAE", "I", "EIO"]
    for word in word_list:
        result = solution(word)
        print(result)