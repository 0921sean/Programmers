def solution(people, limit):
    # 무게순으로 정렬
    people.sort(reverse=True)
    boat = 0
    left = 0
    right = len(people) - 1
    
    while left <= right:
        if people[left] + people[right] <= limit:
            right -= 1
        boat += 1
        left += 1
        
    return boat

# 테스트 케이스
if __name__ == "__main__":
    people_list = [[70, 50, 80, 50], [70, 80, 50]]
    limit_list = [100, 100]
    for people, limit in zip(people_list, limit_list):
        print(solution(people, limit))