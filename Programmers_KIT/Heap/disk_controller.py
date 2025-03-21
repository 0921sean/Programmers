import heapq

def solution(jobs):
    jobs.sort()
    heap = []
    
    current_time = 0    # 현재 시점
    total_time = 0      # 총 반환 시간
    job_index = 0       # jobs 배열에서 처리할 작업 인덱스
    job_count = len(jobs)   # 총 작업 개수

    while job_index < job_count or heap:
        # 현재 시점에서 실행 가능한 작업을 heap에 추가
        while job_index < job_count and jobs[job_index][0] <= current_time:
            start, duration = jobs[job_index]
            heapq.heappush(heap, (duration, start)) # (소요시간, 요청시간) 순서로 저장
            job_index += 1
            
        if heap:    # 실행할 작업이 있다면
            duration, start = heapq.heappop(heap)   # 가장 짧은 작업 선택
            current_time += duration    # 현재 시점 업데이트
            total_time += current_time - start  # 반환 시간 계산
        else:   # 실행할 작업이 없다면
            current_time = jobs[job_index][0]   # 현재 시간을 다음 작업의 요청 시간으로 업데이트
            
    return total_time // job_count

# 테스트 케이스
if __name__ == "__main__":
    jobs_list = [[[0, 3], [1, 9], [2, 6]], [[0, 3], [4, 4], [5, 3], [4, 1]]]
    for jobs in jobs_list:
        result = solution(jobs)
        print(result)