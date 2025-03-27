def solution(n, lost, reserve):
    # 여벌 체육복을 가져온 학생들이 도난당한 경우 처리
    actual_reserve = list(set(reserve) - set(lost))
    actual_lost = list(set(lost) - set(reserve))
    
    answer = n - len(actual_lost)
    
    actual_reserve.sort()
    actual_lost.sort()
    
    for student in actual_lost:
        if student - 1 in actual_reserve:
            actual_reserve.remove(student - 1)
            answer += 1
        elif student + 1 in actual_reserve:
            actual_reserve.remove(student + 1)
            answer += 1
            
    return answer

# 테스트 케이스
if __name__ == "__main__":
    n_list = [5, 5, 3]
    lost_list = [[2, 4], [2, 4], [3]]
    reserve_list = [[1, 3, 5], [3], [1]]
    for n, lost, reserve in zip(n_list, lost_list, reserve_list):
        print(solution(n, lost, reserve))