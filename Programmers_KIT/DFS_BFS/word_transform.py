from collections import deque

def solution(begin, target, words):
    # target이 words 안에 없으면 반환 불가
    if target not in words:
        return 0
    
    def can_transform(word1, word2):
        diff_count = 0
        for c1, c2 in zip(word1, word2):
            if c1 != c2:
                diff_count += 1
        return diff_count == 1
    
    visited = {word: False for word in words}   # 방문 기록
    queue = deque([(begin, 0)]) # (단어, 변환 횟수)
    
    # BFS
    while queue:
        current_word, steps = queue.popleft()
        
        # 현재 단어가 target에 도달하면 변환 횟수 반환
        if current_word == target:
            return steps
        
        for word in words:
            # 거치지 않은 단어고, 한 글자만 다르면
            if not visited[word] and can_transform(current_word, word):
                visited[word] = True
                queue.append((word, steps + 1))
        
    return 0

# Solution 클래스 인스턴스 생성 및 함수 호출
if __name__ == "__main__":
    begin_list = ["hit", "hit"]
    target_list = ["cog", "cog"]
    words_list = [["hot", "dot", "dog", "lot", "log", "cog"], ["hot", "dot", "dog", "lot", "log"]]
    for begin, target, words in zip(begin_list, target_list, words_list):
        result = solution(begin, target, words)
        print(result)