import math

def solution(progresses, speeds):
    left_times = []
    answer = []
    
    for progress, speed in zip(progresses, speeds):
        left_times.append(math.ceil((100 - progress) / speed))
        
    i = 0
    while i < len(left_times):
        first = left_times[i]
        count = 0
        while left_times[i] <= first:
            i += 1
            count += 1
            if i == len(left_times):
                break
        answer.append(count)
        
    return answer

# 테스트 케이스
if __name__ == "__main__":
    progresses_list = [[93, 30, 55], [95, 90, 99, 99, 80, 99]]
    speeds_list = [[1, 30, 5], [1, 1, 1, 1, 1, 1]]
    for progresses, speeds in zip(progresses_list, speeds_list):
        result = solution(progresses, speeds)
        print(result)