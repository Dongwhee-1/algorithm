import heapq

def solution(jobs):
    jobs.sort()
    wait = []
    time = 0
    idx = 0
    total = 0
    count = len(jobs)
    
    while idx < count or wait:
        while idx < count and jobs[idx][0] <= time:
            heapq.heappush(wait, (jobs[idx][1], jobs[idx][0]))
            idx += 1

        if wait:
            work_time, req_time = heapq.heappop(wait)
            time += work_time
            total += time - req_time
        else:
            time = jobs[idx][0]
    return total // count