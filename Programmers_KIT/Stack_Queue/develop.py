import math

def solution(progresses, speeds):
    left_times = []
    answer = []
    
    for i in range(len(progresses)):
        left_times.append(math.ceil((100 - progresses[i]) / speeds[i]))
        
    max_time = left_times[0]
    push_num = 0    # 작업을 동시에 배포하는 개수
    for time in left_times:
        # 만약 현재 작업의 남은 시간이 최대 시간보다 크면, 동시에 배포하는 개수를 업로드하고 초기화
        if time > max_time:
            max_time = time
            answer.append(push_num)
            push_num = 1
        # 만약 현재 작업의 남은 시간이 최대 시간보다 작거나 같으면, 동시에 배포하는 개수를 증가시킴
        else:
            push_num += 1
    # 마지막 작업의 개수를 추가
    answer.append(push_num)
    
    return answer

# 테스트 케이스
if __name__ == "__main__":
    progresses_list = [[93, 30, 55], [95, 90, 99, 99, 80, 99]]
    speeds_list = [[1, 30, 5], [1, 1, 1, 1, 1, 1]]
    for progresses, speeds in zip(progresses_list, speeds_list):
        result = solution(progresses, speeds)
        print(result)