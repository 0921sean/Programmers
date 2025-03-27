def solution(people, limit):
    # 무게순으로 정렬
    people.sort()
    
    left = 0
    right = len(people) - 1
    
    boats = 0
    
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
        else:
            right -= 1
        boats += 1
        
    return boats

# 테스트 케이스
if __name__ == "__main__":
    people_list = [[70, 50, 80, 50], [70, 80, 50]]
    limit_list = [100, 100]
    for people, limit in zip(people_list, limit_list):
        print(solution(people, limit))