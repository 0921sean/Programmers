from collections import deque

def solution(begin, target, words):
    # 주어진 단어 목록에 타겟 단어 없으면 0 반환
    if target not in words:
        return 0
    
    # 단어가 한 글자만 다른지 확인하는 함수
    def can_transform(word1, word2):
        diff_count = 0
        for c1, c2 in zip(word1, word2):
            if c1 != c2:
                diff_count += 1
        return diff_count == 1
    
    visited = {word: False for word in words}
    queue = deque([(begin, 0)])
    
    while queue:
        curr_word, changed = queue.popleft()
        
        if curr_word == target:
            return changed
        
        for word in words:
            if not visited[word] and can_transform(curr_word, word):
                visited[word] = True
                queue.append((word, changed + 1))
                
    return 0

# 테스트 케이스
if __name__ == "__main__":
    begin_list = ["hit", "hit"]
    target_list = ["cog", "cog"]
    words_list = [["hot", "dot", "dog", "lot", "log", "cog"], ["hot", "dot", "dog", "lot", "log"]]
    for begin, target, words in zip(begin_list, target_list, words_list):
        result = solution(begin, target, words)
        print(result)