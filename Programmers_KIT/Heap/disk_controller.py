import heapq

def solution(jobs):
    jobs.sort()
    heap = []
    curr_time = 0   # 현재 시간
    ret_time = 0    # 총 처리 시간
    job_index = 0   # 현재 처리 중인 작업의 인덱스
    job_total = len(jobs)   # 총 작업 수
    
    while job_index < job_total or heap:
        # 현재 시간에 처리할 수 있는 작업을 모두 힙에 추가
        while job_index < job_total and jobs[job_index][0] <= curr_time:
            req_time, cost_time = jobs[job_index]
            heapq.heappush(heap, (cost_time, req_time)) # cost_time 기준 sort되도록
            job_index += 1
        # 현재 시간에 처리할 수 있는 작업이 없다면, 다음 작업의 요청 시간이 현재 시간보다 크면 현재 시간을 갱신
        if not heap:
            curr_time = jobs[job_index][0]
            continue
        # 힙에서 가장 짧은 작업을 꺼내서 처리
        cost_time, req_time = heapq.heappop(heap)
        curr_time += cost_time
        ret_time += curr_time - req_time
    return ret_time // job_total

# 테스트 케이스
if __name__ == "__main__":
    jobs_list = [[[0, 3], [1, 9], [3, 5]], [[0, 3], [4, 4], [5, 3], [4, 1]]]
    for jobs in jobs_list:
        result = solution(jobs)
        print(result)