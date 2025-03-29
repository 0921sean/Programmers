def solution(routes):
    # 차량의 전출 지점을 기준으로 정렬
    routes.sort(key=lambda x: x[1])
    
    camera_count = 1
    camera_position = routes[0][1]
    
    for start, end in routes[1:]:
        if start <= camera_position <= end:
            continue
        else:
            camera_count += 1
            camera_position = end
            
    return camera_count

# 테스트 케이스
if __name__ == "__main__":
    routes_list = [
        [[-20, -15], [-14, -5], [-18, -13], [-5, -3]]
    ]
    
    for routes in routes_list:
        print(solution(routes))