def solution(routes):
    routes.sort(key = lambda x: x[1])
    
    last_camera = -30001
    cameras = 0
    
    for start, end in routes:
        if last_camera < start:
            last_camera = end
            cameras += 1
            
    return cameras

# 테스트 케이스
if __name__ == "__main__":
    routes_list = [
        [[-20, -15], [-14, -5], [-18, -13], [-5, -3]]
    ]
    
    for routes in routes_list:
        print(solution(routes))