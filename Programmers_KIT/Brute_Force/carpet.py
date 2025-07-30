def solution(brown, yellow):
    # total = w * h
    total = brown + yellow
    # w_plus_h = w + h
    w_plus_h = (brown + 4) // 2
    for h in range(1, w_plus_h):
        if total == h * (w_plus_h - h):
            return [w_plus_h - h, h]
            
# 테스트 케이스
brown_list = [10, 8, 24]
yellow_list = [2, 1, 24]
for brown, yellow in zip(brown_list, yellow_list):
    result = solution(brown, yellow)
    print(result)