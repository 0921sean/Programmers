def solution(n, lost, reserve):
    actual_reserve = list(set(reserve) - set(lost))
    actual_lost = list(set(lost) - set(reserve))
    
    for reserve in actual_reserve:
        if reserve - 1 in actual_lost:
            actual_lost.remove(reserve - 1)
        elif reserve + 1 in actual_lost:
            actual_lost.remove(reserve + 1)
            
    return n - len(actual_lost)

# 테스트 케이스
if __name__ == "__main__":
    n_list = [5, 5, 3]
    lost_list = [[2, 4], [2, 4], [3]]
    reserve_list = [[1, 3, 5], [3], [1]]
    for n, lost, reserve in zip(n_list, lost_list, reserve_list):
        print(solution(n, lost, reserve))